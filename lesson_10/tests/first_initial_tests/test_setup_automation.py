import pytest
from assertpy import assert_that


def always_skip():
    return False


class TestInitialSecondSetup:

    @pytest.mark.smoke
    def test_that_user_is_able_to_login(self):
        result: int = 5 + 5
        is_ten: bool = result == 11
        assert_that(is_ten, f"{result} is not equal to expected value").is_true()

    @pytest.mark.xfail
    def test_first_initial_setup_negative_test_c(self):
        result: int = 5 + 5
        assert result == 10

    @pytest.mark.skipif(always_skip(), reason="This test is deprecated.")
    def test_first_initial_setup_negative_test_b(self):
        result: int = 8 + 3
        assert result == 11
