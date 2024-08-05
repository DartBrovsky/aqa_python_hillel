#  builtin functions
from typing import Any

# int_list: list[int] = [1, 0]
#
# result: bool = all(int_list)
#
# result_2: bool = any(int_list)
#
# print(result)
# print(result_2)
#
# byte_array = bytearray(b'Hello, World!')
# print(byte_array)
# print(byte_array[0])
# byte_array[0] = 37
# print(byte_array.decode('utf-8'))
#
# is_callable: bool = callable(6)
#
# print(is_callable)

code = '''
def greet(name):
    print("Hello, " + name)

greet("World")
'''
compiled_code = compile(code, '<string>', 'exec')
exec(compiled_code)


# print(dict(print))

def calculate_if_pair(int_ite: int) -> bool:
    return int_ite % 2 == 0


list_integers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_pairs_integers = list(
    filter(calculate_if_pair, list_integers)
)
new_list = []
for integer in list_integers:
    if integer % 2 == 0:
        new_list.append(integer)

print(list_pairs_integers)

list_pairs_integers: list[int] = [i for i in list_integers if i % 2 == 0]

print(list_pairs_integers)

help(print)

int()


# str_iterator = iter("Hello")
# print(str_iterator)
#
# for e in str_iterator:
#     e


# def create_string_from_integer(n: int) -> str:
#     return str(n)
#
#
# int_list: list[int] = [12, 22, 24]
#
# list_strings = map(str, int_list)

# list_strings = [str(i) for i in int_list]

# new_list = []
# for integer in int_list:
#     str(integer)
#     new_list.append(integer)
#
# for element in list_strings:
#     print(type(element))
# print(next(list_strings))

# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# zipped = zip(list1, list2)
# print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]
# print(dict(zipped))

#  def

def print_my_name() -> None:
    print("My name is Serhii!")


def return_my_age() -> int:
    return 190


print_my_name()
print(return_my_age())


def print_name_of_user(name: str, age: int, title: str = "Junior") -> None:
    print(name)
    print(age)
    print(title)


my_name = "Serhii"
print_name_of_user(my_name, 250, title="Middle")


def users_with_ages(*args: str) -> list[str]:
    return list(args)


print(users_with_ages("1", "3", "7asg", "ahusioughiow"))


def print_kwargs(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Приклад виклику функції
print_kwargs(name="John", age=25, city="New York")

function_my = lambda x, y: x ** y

# print((2, 4)lambda x, y: x ** y)

names_list= [("Max", 24), ("Serj", 30), ("Arte", 18), ("Anton", 29), ("Serj", 14)]

serj_list = list(filter(
    lambda person: person in names_list if person[0] == "Serj" and person[1] >= 15 else None,
    names_list)
)

print(serj_list)
