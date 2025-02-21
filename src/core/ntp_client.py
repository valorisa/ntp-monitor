# src/core/ntp_client.py
import ntplib
import time
from typing import Dict
from ..utils.config_loader import load_config  # Modification ici

class NTPClient:
    def __init__(self):
        self.client = ntplib.NTPClient()
        self.config = load_config()  # Chargement de la config
        self.servers = [s['host'] for s in self.config['ntp_servers']]

    def get_time(self, server: str) -> Dict:
        try:
            response = self.client.request(server, version=4)
            return {
                "offset": response.offset,
                "delay": response.delay,
                "stratum": response.stratum,
                "timestamp": time.time()
            }
        except Exception as e:
            return {"error": str(e)}

    def get_servers(self):
        return self.servers
