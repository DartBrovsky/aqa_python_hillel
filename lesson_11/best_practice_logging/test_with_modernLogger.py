import json
import logging.config
import pathlib

from assertpy import assert_that


def setup_logging():
    config_file = pathlib.Path("your/path/to/file")
    with open(config_file) as file:
        desired_configuration = json.load(file)

    logging.config.dictConfig(desired_configuration)


logger = logging.getLogger(__name__)


class TestWithModernLogger:

    @classmethod
    def setup_class(cls):
        setup_logging()

    def test_is_logger_working(self):
        logger.info("Creation of actual result")
        result = 10 + 10
        logger.info("Creation of expected result")
        expected_result = 20

        logger.info("Test validation")
        assert_that(result).is_equal_to(expected_result)
