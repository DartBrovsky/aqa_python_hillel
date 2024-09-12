import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set the minimum logging level

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the handler's logging level

# Create a formatter and set it for the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)


def log_start_end_test_case(func):
    def wrapper(*args, **kwargs):
        logger.info(f" ")
        logger.info(f"Test {func.__name__} is started")
        result = func(*args, **kwargs)
        logger.info(f"Test {func.__name__} is finished with {result} result")
        return result
    return wrapper


class TestLogDecorator:

    @log_start_end_test_case
    def test_decorator_implementation_positive(self):

        assert 2 == 2

    @log_start_end_test_case
    def test_decorator_implementation_negative(self):

        assert 2 == 3

    @log_start_end_test_case
    def test_decorator_implementation_positive_2(self):

        assert 2 == 2
