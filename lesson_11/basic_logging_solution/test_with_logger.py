import logging
from logging import config

from assertpy import assert_that
import pytest_check as check

# configuration with file
logging.config.fileConfig("logging_config.ini")

# configuration with basic approach
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     handlers=[
#                         logging.StreamHandler(),
#                         logging.FileHandler("example.log")
#                     ])

logger = logging.getLogger(__name__)


class TestWithLogger:

    def test_that_logger_works(self):

        logger.info("Creation of actual result")
        result: int = 10 + 10
        logger.info("Creation of expected result")
        expected_result: int = 20

        logger.info(f"Test validation, {result} with {expected_result}")
        assert_that(result).is_equal_to(expected_result)

        logging.shutdown()

    def test_different_variants(self):
        result_list: list[int] = [10, 10, 3, 10, 10, 5, 10]
        expected_result: int = 10
        for result in result_list:
            # assert_that(result).is_equal_to(expected_result)

            check.is_true(result == expected_result, msg=f"Desired actual result {result} is not equal to desired {expected_result}")