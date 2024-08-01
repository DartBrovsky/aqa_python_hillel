#  condition operators

# age: int = 25
# prof: str = "Doctor"
# name: str = "Anton"
# years_of_work: int = 3
#
# if age == 25 or name == "Serg":
#     print(age)
# elif age > 25:
#     print("More than 25")
# elif 25 > age > 20:
#     print("Less than 25")
# else:
#     print("Not even age: 20")
#
# if (age == 25 or name == "Serg") and (prof == "Engineer" or years_of_work == 5):
#     print("This guy can be Senior Engineer.")

#  cycles

# is_out: bool = True
# counter: int = 0
#
# while is_out == "True":
#     counter += 1
#     print(counter)
#
#     if counter > 5:
#         is_out = False

# symbols: str = "Some string"
# age: list[int] = [20]
# is_old: bool = True
#
# for symbol in age:
#     print(symbol)
#
# my_dict: dict[str, str] = {
#     "name": "Max",
#     "prof": "Engineer"
# }
#
# for key, value in my_dict.items():
#     print(f"{key} : {value}")
#
# for index, char in enumerate(symbols):
#     print(f"This char -> {char} has the next index value -> {index}")

# counter: int = 0
# while True:
#     counter += 1
#     print(counter)
#
#     if counter > 2798:
#         break

for i in range(5):
    if i == 2:
        print("Continue викликаний на i =", i)
        continue
    print(i)
