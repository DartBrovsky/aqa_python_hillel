from lesson_28.core.pages.main_page import MainPage
from lesson_28.core.pages.signup_and_login_page import SignUpAndLoginPage
from lesson_28.core.test_data.test_data import TestData


class TestSignUpAndLogin:
    main_page: MainPage
    sign_up_and_login_page: SignUpAndLoginPage

    def test_that_user_is_able_to_sign_up(self, web_driver):
        self.main_page = MainPage(web_driver)

        self.sign_up_and_login_page = self.main_page.go_to_signup_and_login_page()

        self.sign_up_and_login_page.sign_up_with_credentials(TestData.USER_VALID_NAME, TestData.USER_VALID_EMAIL)


