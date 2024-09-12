from decorators import DecoratorOverview


my_first_decorator_overview: DecoratorOverview = DecoratorOverview(5)

# print(my_first_decorator_overview.decor_value)
#
# my_first_decorator_overview.decor_value = 3
#
# print(my_first_decorator_overview.decor_value)

# del my_first_decorator_overview.decor_value

# print(my_first_decorator_overview.decor_value)

print(my_first_decorator_overview.add_decor_with_another_int(5))
print(my_first_decorator_overview.decor_value)

print(DecoratorOverview.return_received_int(10))
print(my_first_decorator_overview.return_received_int(90))

print(my_first_decorator_overview.increment_by_value(10))



