import json
import paho.mqtt.client as mqtt
import config

class MqttAdapter:
    def __init__(self):
        self.mqtt_endpoints = config.MQTT_ENDPOINTS
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(config.MQTT_HOST, config.MQTT_PORT, keepalive=30)

    def on_connect(self, client, userdata, flags, rc):
        print(f"MQTT connected to {config.MQTT_HOST}:{config.MQTT_PORT}")
        
        for mqtt_endpoint in self.mqtt_endpoints:
            mqtt_status_topic = mqtt_endpoint.get('mqtt_status_topic', None)
            if not mqtt_status_topic:
                continue
            
            title = mqtt_endpoint["title"]
            client.subscribe(mqtt_status_topic)
            
            print(f"Subscribed to {title} on {mqtt_status_topic}")

    def on_disconnect(self, client, userdata, rc):
        print("MQTT disconnected")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
        except json.JSONDecodeError:
            print(f"Payload is not valid JSON toppic {msg.topic}")
            return

        # Kanalnamen ermitteln
        for mqtt_endpoint in self.mqtt_endpoints:
            if mqtt_endpoint.get("mqtt_status_topic", '') == msg.topic or mqtt_endpoint.get("mqtt_set_topic", '') == msg.topic:
                print(f"[{mqtt_endpoint.get('title', '')}] --> Message on topic {msg.topic}: {payload}")

    def loop_start(self):
        self.client.loop_start()

    def loop_stop(self):
        self.client.loop_stop()
