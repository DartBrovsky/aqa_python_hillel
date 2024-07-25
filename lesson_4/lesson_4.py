import re

my_first_string = "<div>My first string</div>"

print(my_first_string[5:-6])

print(my_first_string[::1])

print(len(my_first_string))

my_string_length = len(my_first_string)
print(my_string_length)

if my_string_length == 26:
    print(f"String with value: {my_string_length}\n"
          "is valid")

for symbol in my_first_string:
    print(symbol)

my_new_bigger_string = my_first_string + "2"

print(my_new_bigger_string)

splited_string = "My string with spaces, without others."
print(splited_string.split())
print(splited_string.split(", "))

names_string = "Serhii, Max, Olex, Anton, Oksana"
names_list = names_string.split(", ", 3)

for name in names_list:
    print(name)

print(re.findall("x", names_string))

message = "user, please do not smoke here."
message_2 = "Abuser, please do not smoke here!"

# if message_2.startswith("User,"):
#     print("User is not smoking")
# else:
#     print("User is smoking")

if message_2.endswith("here."):
    print("User is not smoking")
else:
    print("User is smoking")

# print(message_2.islower())
print(message.istitle())
print(message_2.istitle())

print(message.lower())
print(message_2.upper())

print(message.capitalize())
print(message.title())

print(message_2.swapcase())

string_fo_find = "My finding string."
index_of_substring = string_fo_find.find("string")

if index_of_substring != -1:
    print("We successfully found this string")
else:
    print("We are failed with search")

index_of_substring_with_slice = string_fo_find.find("finding", 0, 8)

if index_of_substring_with_slice != -1:
    print("We successfully found this string")
else:
    print("We are failed with search")

message = "User, User please do not smoke here."

abuser_message = message.replace("User", "Abuser", 1)
print(abuser_message)


spaces_message = "    User is able to strip desired string      "

print(spaces_message.strip())
print(spaces_message.lstrip())
print(spaces_message.rstrip())

names_list = ["Oksana", "Nadia", "Veronika"]
spliter = ", "


print(f"All student names: {spliter.join(names_list)}")

age = "30"
age_2 = "30.5"
print(type(age))

int_age = int(age)
print(type(int_age))

float_age = float(int_age)
print(type(float_age))

# print(float(age))
# print(int(int_age))

# age_with_name = "Alex - 39"
# print(int(age_with_name))

names = "Max and Anton"
names_list = names.split("and ")
print(names_list)

print(type(names_list))

names_tuple = tuple(names.split("and "))
names_tuple_2 = tuple(names_list)

print(names_tuple)
print(names_tuple_2)

print(type(names_tuple))
print(type(names_tuple_2))

bool_string = "asklgjklwjg"
boolean = bool(bool_string)

print(type(boolean))
print(boolean)

name = "Max"
age = 18

print(f"User name is {name} and age is {age}")

print(f"Error from this test case has cause: {name}")
print(f"Error from this test case has cause: {{user_cause - {name}}} ")

my_string = "My string for addition info"

print(my_string.isalpha())
my_int_string = "123dsgg"
print(my_int_string.isalnum())
print(my_int_string.isdigit())
my_int_string.isprintable()
my_int_string.casefold()

print(my_string.casefold())


