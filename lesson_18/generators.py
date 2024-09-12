import memory_profiler
import time


first_generator = (x ** 2 for x in range(1, 11))

for item in first_generator:
    print(item)


def simple_generator():
    yield 1
    yield 2
    yield 3


gen = simple_generator()


print(next(gen))
print(next(gen))
print(next(gen))











