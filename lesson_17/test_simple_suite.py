from assertpy import assert_that
from outside_dir import outside_module


class TestSimpleSuite:

    def setup_method(self, method):
        outside_module.print_module_name()
        if method.__name__ == "test_simple_case":
            print("Is equal")

    def test_simple_case(self):

        assert_that(4).is_equal_to(4)

    def test_simple_case_2(self):

        assert_that(4).is_equal_to(3)
