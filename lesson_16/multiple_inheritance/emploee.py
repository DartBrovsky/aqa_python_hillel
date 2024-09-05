from lesson_16.multiple_inheritance.human import Human


class Employee(Human):

    is_live: bool = False
    __seniority: str
    __specialization: str

    def __init__(self, seniority: str, specialization: str, legs: int, hands: int):
        Human.__init__(self, legs, hands)
        self.__seniority = seniority
        self.__specialization = specialization

    @property
    def get_employee_seniority(self) -> str:
        return self.__seniority

    @property
    def get_employee_specialization(self) -> str:
        return self.__specialization
