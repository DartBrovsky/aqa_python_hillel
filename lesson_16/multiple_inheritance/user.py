from lesson_16.multiple_inheritance.emploee import Employee
from lesson_16.multiple_inheritance.person import Person


class User(Person, Employee):
    def __init__(self, name: str, age: int, seniority: str, specialization: str, legs: int, hands: int):

        Person.__init__(self, name, age, legs, hands)
        Employee.__init__(self, seniority, specialization, legs, hands)

    def print_user_data(self) -> None:
        print(f"User with name {self.get_person_name} and age {self.get_person_age} is working as "
              f"{self.get_employee_specialization} on {self.get_employee_seniority} position. "
              f"and has {self.legs} legs and {self.hands} hands")

    def get_is_alive_status(self):
        print(f"Person.is_live: {Person.is_live}")
        print(f"Employee.is_live: {Employee.is_live}")


arsen_user: User = User("Serhii", 104, "Lector", "QA Automation Python", 2, 2)

arsen_user.print_user_data()

arsen_user.get_is_alive_status()
