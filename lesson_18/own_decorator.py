

def own_decorator(func):
    def wrapper():
        print("This decorator function before realization..............")
        func()
        print("This decorator function after realization...............")

    return wrapper


def before_decorator(func):
    def wrapper():
        print("This decorator function before realization..............")
        func()

    return wrapper


def after_decorator(func):
    def wrapper():
        func()
        print("This decorator function after realization...............")

    return wrapper


@before_decorator
@after_decorator
def decorated_func():
    print("This function is decorated..............................")


decorated_func()

