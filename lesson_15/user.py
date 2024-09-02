class User:
    name: str = "Default User`s name"
    age: int = 100
    _credit_card_number: str = "0000 1111 2222 3333"
    __cvv_number: int = 650

    def __init__(self, name: str, age: int, credit_card_number: str, cvv_number: int) -> None:
        self.name = name
        self.age = age
        self._credit_card_number = credit_card_number
        self.__cvv_number = cvv_number

        self.__payment()

    @property
    def get_credit_card_number(self):
        return self._credit_card_number

    def __payment(self):
        return self.__cvv_number and self._credit_card_number

    def pay(self) -> None:
        self.__payment()


    # def __str__(self) -> str:
    #     return f"User with name {self.name} and age {self.age}"
    #
    # def __len__(self) -> int:
    #     return len(self.name)
    #
    # def __add__(self, other_age) -> int:
    #     return self.age + other_age.age
    #
    # def __lt__(self, other):
    #     return self.age < other.age
    #
    # def __gt__(self, other):
    #     return self.age > other.age
    #
    # def __contains__(self, item) -> bool:
    #     return item in self.name
    #
    # def __getitem__(self, item) -> object:
    #     if item == "name":
    #         return self.name
    #     elif item == 'age':
    #         return self.age
    #
    # def __eq__(self, other) -> bool:
    #     return self.name == other.name and self.age == other.age
    #
    # def __setattr__(self, key, value):
    #     print(f"We changed attribute {key} into value {value}")
    #     super.__setattr__(self, key, value)
    #
    # def __delattr__(self, item):
    #     if item == 'age':
    #         raise PermissionError(f"We are not able to delete attribute {item}")
    #     else:
    #         super.__delattr__(self, item)

    def print_user_name(self) -> None:
        print(self.name)

    # def __del__(self):

    #     print(f"Attributes name {self.name} and age {self.age} were destructed.")

class SchoolUser(User):

    def set_card_number(self, new_number: str) -> None:
        self._credit_card_number = new_number

class UniversityUser(User):

    ...


