import mqtt_adapter

# callbacks.py
def mqtt_test_callback(payload, endpoint, self):
    print(f"[mqtt_test_callback for {endpoint.get('title', '')}] --> {payload}")


def mqtt_MQTTTest_callback(payload, endpoint, adapter: mqtt_adapter.MqttAdapter=None):
    print(f"[mqtt_MQTTTest_callback for {endpoint.get('title', '')}] --> {payload}")
    if adapter:
        value = payload.get("v")
        
        response_value = {"v": value}        
        adapter.send_set('Licht Gartenseite:Aktor:2 - STATE', response_value)
        adapter.send_set('Licht Strassenseite:Aktor:2 - STATE', response_value)
