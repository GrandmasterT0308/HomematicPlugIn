import requests
import urllib3
import config

# Warnungen bei selbstsignierten Zertifikaten deaktivieren
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RestClient:
    def __init__(self):
        self.base_url = f'https://{config.REST_HOST}:{config.REST_PORT}'
