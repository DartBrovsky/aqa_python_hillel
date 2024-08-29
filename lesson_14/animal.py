from abc import ABC, abstractmethod


class Animal(ABC):

    height: int
    weight: int

    def __init__(self, height: int, weight: int):
        self.height = height
        self.weight = weight

    @abstractmethod
    def speak(self):
        ...

    def damage(self):
        print("Abstract damage")

