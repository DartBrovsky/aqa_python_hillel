# Exception handling

# def divide(a, b):
#     # return a / b
#     try:
#         return a / b
#     except ZeroDivisionError as e:
#         print(f"Помилка ділення на нуль: {e}")
#     finally:
#         print("Program is done.")


# def try_to_connect_to_db(config: dict[str, object]):
#     try:
#         session.connect(config)
#     except ConnectionError as exception:
#         print(exception.args)
#     finally:
#         session.close()

# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except (ZeroDivisionError, TypeError) as exception:
#         print(f"Помилка: Ділення на нуль. {exception}")
#     # except TypeError as exception:
#     #     print(f"Int to string division: {exception}")
#     # except Exception as exception:
#     #     print(f"We`ve been raised by next exception: {exception}")
#     else:
#         print(f"Результат ділення {a} на {b}: {result}")
#     finally:
#         print("Our program is done...")
#
#
# divide_numbers(10, 2)
# divide_numbers(5, 0)
# divide_numbers(5, "asdf")

# divide(10, 2)

# def check_age(age):
#     if age < 0:
#         raise ValueError("Вік не може бути від'ємним")
#
#
# try:
#     user_age = int(input("Введіть ваш вік: "))
#     check_age(user_age)
#     print(f"Ваш вік: {user_age}")
# except ValueError as ve:
#     print(f"Помилка: {ve}")

class TestFrameworkException(Exception):
    def __init__(self, reason: str, value: int):
        self.reason = reason
        self.value = value
        message: str = f"Raised Framework Exception due to: {reason} with {value}"
        super().__init__(message)


def is_in_list(expected_list: list[int]):
    for item in expected_list:
        if item == 0:
            raise TestFrameworkException("We found the next invalid value -> ", item)
        else:
            print(f"We are good with value: {item}")


is_in_list([1, 4, 6])
is_in_list([2, 0, 4])
