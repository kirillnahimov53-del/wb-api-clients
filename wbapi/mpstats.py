import requests
from .base import BaseClient

class MPStatsClient(BaseClient):
    def __init__(self):
        super().__init__("MPSTATS_API_KEY", "https://mpstats.io")

    def ping(self):
        url = f"{self.base_url}/api/some-ping"
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        return r.json()
