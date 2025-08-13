import requests
from .base import BaseClient

class WildberriesClient(BaseClient):
    def __init__(self):
        super().__init__("WB_API_TOKEN", "https://statistics-api.wildberries.ru")

    def get_sales(self, date_from: str):
        """
        Заглушка под реальные эндпоинты.
        date_from: "2025-08-01T00:00:00Z"
        """
        url = f"{self.base_url}/api/v1/supplier/sales"
        # params/headers зависят от актуального эндпоинта
        resp = requests.get(url, headers=self.headers, params={"dateFrom": date_from})
        resp.raise_for_status()
        return resp.json()
