

class DecoratorOverview:

    __decor: int = 10

    def __init__(self, decor: int) -> None:
        self.__decor = decor

    @staticmethod
    def return_received_int(received_int: int):
        return received_int

    @classmethod
    def increment_by_value(cls, increment: int):
        return cls.__decor + increment

    @property
    def decor_value(self) -> int:
        return self.__decor

    @decor_value.setter
    def decor_value(self, decor: int) -> None:
        self.__decor = decor

    @decor_value.deleter
    def decor_value(self) -> None:
        del self.__decor

    def add_decor_with_another_int(self, external_int: int) -> int:
        return self.__decor + external_int


