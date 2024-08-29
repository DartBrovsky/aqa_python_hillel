from typing import override

from lesson_14.animal import Animal


class Cat(Animal):
    ...

    life_counter: int = 9

    def __init__(self, height: int, weight: int, life_counter: int):
        super().__init__(height, weight)
        self.life_counter = life_counter

    def speak(self):
        print("meow")

    @override
    def damage(self):
        print("You are sick and have no 9 lives")

