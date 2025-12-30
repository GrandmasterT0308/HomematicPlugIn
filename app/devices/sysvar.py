from devices.base import BaseEndpoint

class SysVar(BaseEndpoint):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

        self.mqtt_status_topic = f"sysvar/status/{address}"
        self.mqtt_set_topic = f"sysvar/set/{address}"
