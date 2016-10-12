from abc import ABCMeta, abstractmethod

class Electronic ( object ):
    """A class that has the basic requirement for all electronics
     i,e power connection and ability to switch on and off
    """

    __metaclass__ = ABCMeta

    def __init__ (self,):
        self.power = "disconnect"

    @abstractmethod
    def power_connection ( self, connection ):
        pass

    def switch_on ( self ):
        raise NotImplementedError("Subclass must implement switch_on() method. ")

    def switch_off ( self ):
        raise NotImplementedError("Subclass must implement swtch_off() method. ")




class Radio ( Electronic ):
    """A class to instantiates a radio It takes in arguments that depict
    the make, and model of the Radio, provided they are set
    It has methods for switching on, setting the voloume,
    setting channel, switching off and power_connection.
    It has attributes such as status, volume, channel and power
    """


    def __init__ ( self, make = 'unknown', model = "unknown", ):
        """The constructor"""
        Electronic.__init__( self )
        self.state = "OFF"
        self.volume = 0.0
        self.channel = 0.0

    def switch_on ( self ):
        """Used to switch on the radio"""
        if self.power == "disconnect":
            return "Please connect power first via .power_connection ('connect')"
        if self.state == "ON":
            return "Radio is already on, channel: %f volume: %f" %(self.channel,
                                                                   self.volume )
        else:
            self.state = "ON"
            self.channel = 87.5
            self.volume = 0.0
        return " status: ON channel: 87.5 volume: 0"

    def set_voloume ( self, vol ):
        """Sets volume to a value between 0 and 100"""
        if self.state == "OFF": return "This Radio is off"
        if not (isinstance(vol, int) or isinstance(vol, float)):
            raise ValueError("Volume MUST be a number")
        if 0 <= vol <=100 and self.state == "ON":
            self.volume = float(vol)
            return "Volume: %0.1f" %(self.volume)
        else:
            return "Sorry, You can only set a volume value that is between 0.0 and 100.0"

    def set_channel ( self, frequency ):
        """Sets channel to a value between 87.5 and 108.0"""
        if self.state == "OFF": return "This Radio is off"
        if not (isinstance(frequency, int) or isinstance(frequency, float)):
            raise ValueError("Channel MUST be a number")
        if 87.5 <= frequency <= 108:
            self.channel = float(frequency)
            return "Channel: %0.1f" %(self.channel)
        else:
            return "The channel must be between 87.5 and 108.0"

    def power_connection ( self, connection ):
        """Connects and disconnects power supply"""
        if connection in ( "connect", "disconnect" ):
            self.power = connection
            print "%sed" %(self.power)
        else:
            raise ValueError("The argument MUST be either 'connect' or 'disconnect")
        if connection == "disconnect":
            self.state = "OFF"
            self.volume = 0.0
            self.channel = 0.0

    def switch_off ( self ):
        """Used to switch off the radio"""
        if self.power == "disconnect":
            return "The Radio is OFF and power is disconnected "
        if self.state == "OFF":
            return "The Radio is OFF but power is connected "
        else:
            self.status = "OFF"
            self.channel = 0.0
            self.volume = 0.0
        return " status: OFF "

    def status(self,):
        """Used to check the status, channel and volume of the Radio"""
        if self.state == "OFF":
            return " status: OFF"
        return " status: ON channel: 87.5 volume: 0"




