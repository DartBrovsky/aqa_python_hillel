from abc import ABC, abstractmethod


class AbstractApiService(ABC):

    @staticmethod
    @abstractmethod
    def post_item(final_endpoint: str, data: dict[str, object]):
        ...

    @staticmethod
    @abstractmethod
    def put_item(final_endpoint: str, data: dict[str, object]):
        ...

    @staticmethod
    @abstractmethod
    def get_item(final_endpoint: str):
        ...

    @staticmethod
    @abstractmethod
    def delete_item(final_endpoint: str):
        ...


