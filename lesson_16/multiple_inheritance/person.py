from lesson_16.multiple_inheritance.human import Human


class Person(Human):

    is_live: bool = True
    __name: str
    __age: int

    def __init__(self, name: str, age: int, legs: int, hands: int):
        Human.__init__(self, legs, hands)
        self.__name = name
        self.__age = age

    @property
    def get_person_name(self) -> str:
        return self.__name

    @property
    def get_person_age(self) -> int:
        return self.__age
