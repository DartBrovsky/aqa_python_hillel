name = "Serhii"
name_2 = 'Alex'
age = 16

print(name,
      age)

'''agklsjkljgasklgjklajsdklgjadsjgklajsdklgjaklsjgklajsgkljasklgjklasjgklajsgklajklgj
ajsklgjaklsjgklajsgklajgklsjaklsjgklajsgklj'''

age = 10
age_2 = 3

print(age)
print(age_2)

average_age = int(age / age_2)
average_age_2 = age // age_2
last_result = age % age_2
result = age ** age_2

# print(average_age)
print(average_age_2)
print(last_result)
print(result)

is_true = True
is_false = False

print()

if age == "10":
    print(age)

# my_tuple = (1, 2, 3)
#
# print("My name: "
#       "Serhii")
# status = "Completed"
#
# print(status[-1])
# size_of_sequence = len(status)
# last_symbol_index = len(status) - 1
#
# print(status[last_symbol_index])
#
# for symbol in status:
#     print(symbol)

my_tuple = (1, 2, 3)
my_tuple2 = tuple()

print(my_tuple[-1])

my_list = ["Alex", "Anton", "Serhii"]
# my_list_2 = list(["Alex", "Anton", "Serhii", "Max"])

print(my_list)
my_list.append("Max")
print(my_list)
my_list.remove("Max")
print(my_list)
for name in my_list:
    print(name)

# my_set = {1, 2, 3, 3}
# # my_set = set()
# print(my_set)
# print(my_set)
# print(my_set)
#
# my_dict = {"name": "Serhii",
#            "age": "90"}
#
# print(my_dict["age"])
a = "one"
b = "one"

if a == b:
    print("Yes")

users_dict = {"Serhii": 67,
              "Max": 43}

for age, name in enumerate(users_dict):
    print(f"Current User name is: {name} \n"
          f"Current User age is: {age}")

user_age = int(input("Fill your age here: "))

if user_age == 36:
    print(f"User name is : {user_age}")
