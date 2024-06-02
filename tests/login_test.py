from tests.base_test import BaseTest
from pages import main_page, login_page
from time import sleep


class LoginTest(BaseTest):

    def test1_correct_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
