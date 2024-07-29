#  Tuple

my_tuple = tuple()
my_tuple_1 = (1, 4, "Name", 4.8, True)

first, *middle, last = my_tuple_1
print(first)
print(middle)

print(my_tuple_1)
print(type(my_tuple_1))

print(my_tuple_1[0])
print(my_tuple_1[-1])
print(my_tuple_1[2])

print(my_tuple_1.count("Name"))

print(my_tuple_1.index(1))

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(my_tuple[5:-1])
print(my_tuple[0:-1:2])

reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

my_string = "I learn tuples"

my_string_tuple = tuple(my_string)
print(my_string_tuple)

my_list = [1, 2, 3, 'Python', True]
tuple_from_list = tuple(my_list)

print(tuple_from_list)

#  List

# my_list = []
# my_list_1 = list()
#
# diff_types_list = [(1, 2, 4), 1, 3, 2.4, True, "Main", 2]
# print(diff_types_list)
#
# print(diff_types_list[-1])
# print(diff_types_list[0:-1:2])
#
# diff_types_list.append("New Item")
#
# print(diff_types_list)
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list2.extend(list1)
# print(list2)

# my_list = [1, 2, 3]
# my_list.insert(0, 4)
# print(my_list)

# my_list = [1, 2, 2, 3, 2]
# my_list.remove(2)
# print(my_list)
#
# my_list = [1, 2, 3, 4]
# popped_element = my_list.pop(3)
#
# print(my_list)
# print(popped_element)

# my_list = [1, 2, 3, 2]
# index_of_2 = my_list.index(1)
# print(index_of_2)
#
# my_list = [1, 2, 3, 2, 5, 2]
# count_of_2 = my_list.count(2)
# print(count_of_2)
#
# my_list[2] = "Name"
# my_list.insert(2, "Name")
# print(my_list)
#
# numbers = [1, 2, 3, 4, 5]
# numbers_2 = [1, 5, 3, 5]
#
# first_element, *middle, lasted = numbers_2
#
# print("Перший елемент:", first_element)
# print("Серединні елементи:", middle)
# print("Останній елемент:", lasted)
#
# numbers_2 = [5, 2, 8, 1, 3]
# numbers_2.sort(reverse=True)
# print(numbers_2)
#
#
# numbers = [5, 2, 8, 1, 3]
# sorted_numbers = sorted(numbers, reverse=True)
# print(numbers)
# print("Відсортований список:", sorted_numbers)
#
# names_list = ["Serhii", "Max", "Oleksandr", "Anton"]
# len_sorted_list = sorted(names_list, key=lambda x: len(x), reverse=True)
#
# print(len_sorted_list)
#
# my_string = "My string to list"
# list_from_string = list(my_string)
# print(list_from_string)
#
# my_range = range(1, 6)
# print(my_range)
# list_from_range = list(my_range)
# print(list_from_range)
#
# my_tuple = (10, 20, 30, 40, 50)
# list_from_tuple = list(my_tuple)
# print(list_from_tuple)
my_string = "Na string"
my_list = list(my_string)

squares = [symbol for symbol in "my_tuple"]
print(squares)

list_of_pairs = [integer for integer in range(0, 11) if integer % 2 == 0]
print(list_of_pairs)

new_list = []
for integer in range(0, 11):
    if integer % 2 == 0:
        new_list.append(integer)

first_list = [1, 2]
second_list = first_list
second_list_new = list(first_list)
second_list.append(3)

print(first_list)
print(second_list)

#  Set

fruits = {"apple", "cherry"}
fruits_2 = set()

print(hash("string"))

my_set = {1, 2, 3, 4, 5}
element = 3

if element in my_set:
    print(element)
else:
    print("None")

# poped_element = my_set.pop()
# print(poped_element)

my_set.remove(1)
print(my_set)

my_set = {1, 2, 3}
additional_elements = {4, 5, 6}
my_set.update(additional_elements)
print(f"Оновлена множина: {my_set}")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

logical_union = set1.union(set2)
# або
logical_union = set1 | set2

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(logical_union)

logical_intersection = set1.intersection(set2)
# або
logical_intersection = set1 & set2
print(logical_intersection)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

logical_difference = set1.difference(set2)
# або
logical_difference = set1 - set2
print(logical_difference)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

logical_symmetric_difference = set1.symmetric_difference(set2)
# або
logical_symmetric_difference = set1 ^ set2

print(logical_symmetric_difference)

my_list = [1, 2, 3, 3, 4, 5]
set_from_list = set(my_list)
print(set_from_list)

numbers = [1, 2, 2, 3, 3, 4, 5, 5]


#  Dict

dict_my = {'1_key': "Name",
           '2nd_key': "Date"
        }

dict_my_2 = dict()

dict_list_key = {
    (1, 2): 1,
    '1_key': "Name",
    2: 2
}

dict_my_new = {
    '1_key': "Name",
    '2nd_key': ["Date", "Age"]
}

print(dict_my_new["1_key"])
print(dict_my_new.get('1_key'))
print(dict_my_new["2nd_key"])

keys = dict_my_new.keys()
values = dict_my_new.values()
items_from_dict = dict_my_new.items()

print(keys)
print(values)
print(items_from_dict)

my_dict = {'ключ1':1, 'ключ2':2, 'ключ3':3}
my_dict.clear() # {}

print(my_dict)

my_dict = {'ключ1':1, 'ключ2':2, 'ключ3':3}
кортеж_ключ_значення = my_dict.popitem()

# кортеж_ключ_значення = ('ключ2',2)

my_dict = {'ключ1':1, 'ключ2':2, 'ключ3':3}
інший_словник = {'ключ1':1 , 'ключ4':4}
my_dict.update(інший_словник)

my_dict = {'ключ1':1, 'ключ2':2, 'ключ3':3}
інший_словник = {'ключ1':1 , 'ключ4':4}
my_dict.update(інший_словник)

print(my_dict)

# for key, value in my_dict.items():
#     print(key, value)
#     del my_dict[key]

список_кортежів = [('ключ1', 'значення1'), ('ключ2', 'значення2'), ('ключ3', 'значення3')]
словник = dict(список_кортежів)

ключі = ['ключ1', 'ключ2', 'ключ3']
значення = ['значення1', 'значення2', 'значення3']
словник = dict(zip(ключі, значення))


dict_my_3 = {x: x**2 for x in range(10) if x % 2 == 0}
print(dict_my_3)
print(dict_my_3.items())




