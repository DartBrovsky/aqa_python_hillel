from assertpy import assert_that

from lesson_27.page_object.MainPage import MainPage
from lesson_27.page_object.login_page import LogInPage
from lesson_27.test.conftest import create_driver


class TestLogIn:
    main_page: MainPage
    login_page: LogInPage

    def test_that_user_is_able_to_log_in(self, create_driver):
        self.main_page = MainPage(create_driver)
        self.login_page = self.main_page.go_to_login_page()

        (self.login_page
         .fill_login_data()
         .click_on_log_in_button())

        self.main_page.verify_that_user_is_logged_in()
