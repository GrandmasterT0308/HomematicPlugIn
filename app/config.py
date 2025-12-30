MQTT_HOST = "192.168.2.111"
MQTT_PORT = 1883

REST_HOST = "192.168.2.111"
REST_PORT = 2122

# Beispieltopic, an das das Plugin sich subscribt
MQTT_ENDPOINTS = [
    {
        "title": "Licht Gartenseite:Aktor:2 - STATE",
        "mqtt_status_topic": "device/status/000B9A498D76F0/2/STATE",
        "mqtt_set_topic": "device/set/000B9A498D76F0/2/STATE",
        "devicetype": "device",
        "callback": "callbacks.mqtt_test_callback"
    },
    {
        "title": "Licht Strassenseite:Aktor:2 - STATE",
        "mqtt_status_topic": "device/status/000B9A498D747D/2/STATE",
        "mqtt_set_topic": "device/set/000B9A498D747D/2/STATE",
        "devicetype": "device",
        "callback": "callbacks.mqtt_test_callback"
    },
    {
        "title": "MQTT.Test",
        "mqtt_status_topic": "sysvar/status/9292",
        "mqtt_set_topic": "sysvar/set/9292",
        "devicetype": "sysvar",
        "callback": "callbacks.mqtt_MQTTTest_callback"
    }
]