# from lesson_9_external_func.sum_and_return import sum_and_return

# from importlib.machinery import SourceFileLoader
# module_name = 'sum_and_return'
#
# desired_module = SourceFileLoader(module_name, "/Users/dart_brovsky/PycharmProjects"
#                                                "/aqa_python_hillel/lesson_9_external_func/sum_and_return.py").load_module()

# import sys
# import pathlib
# sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
# from folder.main_module import add

from unittest import TestCase

from lesson_9.lesson_9_external_func.sum_and_return import sum_and_return


# class MyTest(TestCase):
#
#     def test_if_sum_is_equal_to_ten(self):
#         result: int = sum_and_return(5, 5)
#
#         self.assertEqual(result, 10)

class AssertionTesting(TestCase):

    def test_if_sum_is_equal_to_ten(self):
        result: int = sum_and_return(5, 5)

        self.assertEqual(result, 10)

    def get_name_and_check(self, name: str):
        return name

    def test_that_user_name_is_equal_to_expected(self):
        desired_name = self.get_name_and_check("Serdhii")

        self.assertEqual(desired_name, "Serhii")

    def test_that_user_name_is_in_list(self):
        list_of_names = ["Serhii", "Max", "Nadia"]

        is_inside_list: bool = "Serhii" in list_of_names
        self.assertTrue(is_inside_list)

        # self.assertTrue(not is_inside_list)
        # self.assertFalse(is_inside_list)
        self.assertIn("Serhiig", list_of_names,
                      msg=f"User name Serhii is not in list of desired name from MySql db: \n"
                          f"{list_of_names}")

        # assert "Serhigi" in list_of_names


import unittest


def divide(x, y):
    return x / y


class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = divide(5, 0)


if __name__ == '__main__':
    unittest.main(verbosity=0)
