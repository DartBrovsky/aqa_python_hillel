from lesson_14.animal import Animal
from lesson_14.cat import Cat
from lesson_14.dog import Dog

# first_animal: Animal = Animal(50, 30)
dog: Dog = Dog(30, 20, 1)
cat: Cat = Cat(15, 8, 5)

# print(first_animal.weight)
print(cat.weight)
print(dog.weight)
print(type(dog))

# first_animal.speak()
cat.speak()
print(Cat.life_counter)
print(cat.life_counter)
dog.speak()

dog.damage()
dog.damage(10)



