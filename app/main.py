from mqtt_adapter import MqttAdapter
import config

def main():

    # MQTT Adapter starten
    adapter = MqttAdapter()

    print("MQTT Plugin running. Press Ctrl+C to exit.")
    try:
        adapter.client.loop_forever()
    
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
