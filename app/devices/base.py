class BaseEndpoint:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.mqtt_status_topic = None
        self.mqtt_set_topic = None

    def on_message(self, payload, adapter):
        """
        Wird vom MQTT-Adapter aufgerufen
        """
        new_value = payload.get("v") if isinstance(payload, dict) else payload
        if new_value != self.value:
            self.value = new_value
            print(f"[{self.name}] Value changed to {self.value}")
            self.on_change(new_value, adapter)

    def on_change(self, value, adapter):
        """
        Kann von Subklassen überschrieben werden
        """
        pass
