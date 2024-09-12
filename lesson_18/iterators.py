

first_iterator = iter([1, 2, 3, 4, 5])

print(first_iterator)

print(next(first_iterator))
print(next(first_iterator))
print(next(first_iterator))
print(next(first_iterator))
print(next(first_iterator))

try:
    print(next(first_iterator))
except StopIteration as exception:
    print("This iterator was finished and has no new elements.")


class CustomIterator:

    __current: int = 0
    __max_num: int

    def __init__(self, max_num: int) -> None:
        self.__max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current < self.__max_num:
            self.__current += 1
            return self.__current
        else:
            raise StopIteration(f"Iteration was stopped after last value {self.__current} was extracted.")


custom_iterator: CustomIterator = CustomIterator(5)

for num in custom_iterator:
    print(num)

# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
#
# try:
#     print(next(custom_iterator))
# except StopIteration as exception:
#     print(exception)

