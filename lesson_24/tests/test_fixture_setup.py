from operator import add

import pytest


@pytest.mark.usefixtures("log_2", "log")
class TestFixtureSetup:

    def test_initial_fixture(self, my_first_fixture):
        assert my_first_fixture % 2 == 0

    def test_second_fixture(self, my_first_fixture):
        assert my_first_fixture % 2 == 0

    @pytest.mark.parametrize("x, y, expected", [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5)
    ])
    def test_addition(self, x, y, expected):
        result = add(x, y)
        assert result == expected
