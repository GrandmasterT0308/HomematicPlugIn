from devices.base import BaseEndpoint

class Device(BaseEndpoint):
    
    def __init__(self, name, address, channel, parameter):
        super().__init__(name)
        self.address = address
        self.channel = channel
        self.parameter = parameter

        self.mqtt_status_topic = f"device/status/{address}/{channel}/{parameter}"
        self.mqtt_set_topic = f"device/set/{address}/{channel}/{parameter}"
