import json

import requests
from requests import Response


class APIClient:

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_data(self) -> json:
        endpoint_url: str = f"{self.base_url}/data"

        response: Response = requests.get(endpoint_url)
        return response.json() if response.status_code == 200 else None
