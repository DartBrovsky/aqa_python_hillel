import itertools
import unittest


def add(a, b):
    return a + b


class TestAddFunction(unittest.TestCase):

    def test_add(self):
        test_data = itertools.product([1, 2, 3], [4, 5, 6])

        for a, b in test_data:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), a + b)


if __name__ == "__main__":
    unittest.main()
