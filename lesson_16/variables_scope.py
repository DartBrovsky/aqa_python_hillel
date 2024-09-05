
global_string_variable: str = "Global string variable"
global_int_variable = None


def print_global_variable():
    global_string_variable

    global global_int_variable
    global_int_variable = 1
    print(global_int_variable)


def assign_non_local_variable():
    non_local_str_variable: str = "Non local string variable"
    print(non_local_str_variable)

    def another_func():
        non_local_str_variable

    if isinstance(non_local_str_variable, str):
        print(non_local_str_variable)

        if len(non_local_str_variable) > 25:
            non_local_str_variable = ""
            print(non_local_str_variable)


def assign_local_variable():
    local_str_variable: str = "Local string variable"
    print(local_str_variable)


global_string_variable


class VariablesScope:

    global_string_variable_clazz: str = "Global string variable of current clazz"

    def __init__(self):
        print(self.global_string_variable_clazz)

    def try_something(self):
        local_variable: str = "Local variable"

        try:
            print(local_variable)
        finally:
            print(local_variable)

        print(local_variable)


