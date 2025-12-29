from rest_client import RestClient
from mqtt_adapter import MqttAdapter
import config

def main():

    # MQTT Adapter starten
    adapter = MqttAdapter()
    adapter.loop_start()

    print("MQTT Plugin running. Press Ctrl+C to exit.")
    try:
        while True:
            pass
    
    except KeyboardInterrupt:
        print("Exiting...")

    adapter.loop_stop()

if __name__ == "__main__":
    main()
