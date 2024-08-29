from typing import override

from lesson_14.animal import Animal


class Dog(Animal):

    life_counter: int = 1

    def __init__(self, height: int, weight: int, life_counter: int):
        super().__init__(height, weight)
        self.life_counter = life_counter

    def speak(self):
        print("Raph")

    @override
    def damage(self):
        print("You are sick")
