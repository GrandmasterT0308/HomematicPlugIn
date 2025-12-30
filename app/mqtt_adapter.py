import json
import paho.mqtt.client as mqtt
import config
from devices import DEVICES
from devices.base import BaseEndpoint

class MqttAdapter:
    def __init__(self):
        self.devices = DEVICES
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(config.MQTT_HOST, config.MQTT_PORT, keepalive=30)

    def on_connect(self, client, userdata, flags, rc):
        print(f"[MqttAdapter] MQTT connected to {config.MQTT_HOST}:{config.MQTT_PORT}")
        
        for mqtt_device in self.devices:
            if not mqtt_device.mqtt_status_topic:
                continue
            
            client.subscribe(mqtt_device.mqtt_status_topic)
            print(f"[MqttAdapter] Subscribed to {mqtt_device.name} on {mqtt_device.mqtt_status_topic}")

    def on_disconnect(self, client, userdata, rc):
        print("[MqttAdapter] MQTT disconnected")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
        except json.JSONDecodeError:
            print(f"[MqttAdapter] Payload is not valid JSON toppic {msg.topic}")
            return

        # Kanalnamen ermitteln
        print(f"[MqttAdapter] Message on topic {msg.topic}: {payload}")
        for mqtt_device in self.devices:
            if mqtt_device.mqtt_status_topic == msg.topic:                
                mqtt_device.on_message(payload, self)
        
        return

    def loop_start(self):
        self.client.loop_start()

    def loop_stop(self):
        self.client.loop_stop()