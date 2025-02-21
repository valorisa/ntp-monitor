import ntplib
import time
from typing import Dict

class NTPClient:
    def __init__(self):
        self.client = ntplib.NTPClient()

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

if __name__ == "__main__":
    client = NTPClient()
    result = client.get_time("pool.ntp.org")
    print(result)
