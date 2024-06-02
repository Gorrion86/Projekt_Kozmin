from tests.base_test import BaseTest
from pages import main_page, login_page, my_account_page
from time import sleep


class LoginTest(BaseTest):

    def test1_login_page_content_visible(self):
        main_page.go_to_login_page(self.driver)
        self.assertTrue(login_page.login_page_content_visible(self.driver))

    def test2_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(my_account_page.my_account_header_visible(self.driver))

    def test3_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.incorrect_login(self.driver)
        self.assertTrue(login_page.login_error_visible(self.driver))