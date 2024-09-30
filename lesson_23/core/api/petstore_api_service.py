import requests
from requests import Response

from lesson_23.core.api.abstract_api_service import AbstractApiService


class PetstoreApiService(AbstractApiService):

    BASE_URL: str = "https://petstore.swagger.io/v2/"
    BASE_HEADER: dict[str, str] = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    @staticmethod
    def post_item(final_endpoint: str, data: dict[str, object]) -> Response:
        return requests.post(f"{PetstoreApiService.BASE_URL}{final_endpoint}", headers=PetstoreApiService.BASE_HEADER,
                             data=data)

    @staticmethod
    def put_item(final_endpoint: str, data: dict[str, object]) -> Response:
        return requests.put(f"{PetstoreApiService.BASE_URL}{final_endpoint}", headers=PetstoreApiService.BASE_HEADER,
                            data=data)

    @staticmethod
    def get_item(final_endpoint: str) -> Response:
        return requests.get(f"{PetstoreApiService.BASE_URL}{final_endpoint}", headers=PetstoreApiService.BASE_HEADER)

    @staticmethod
    def delete_item(final_endpoint: str) -> Response:
        return requests.delete(f"{PetstoreApiService.BASE_URL}{final_endpoint}", headers=PetstoreApiService.BASE_HEADER)

    @staticmethod
    def delete_item_with_parameters(final_endpoint: str, params: dict[str, str]) -> Response:
        return requests.delete(f"{PetstoreApiService.BASE_URL}{final_endpoint}", headers=PetstoreApiService.BASE_HEADER,
                               params=params)
