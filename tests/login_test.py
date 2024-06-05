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
        self.assertTrue(my_account_page.my_account_content_visible(self.driver))

    def test3_incorrect_login(self):
        main_page.go_to_login_page(self.driver)
        login_page.incorrect_login(self.driver)
        self.assertTrue(login_page.wrong_login_alert_visible(self.driver))

    def test4_empty_email_registration_attempt(self):
        main_page.go_to_login_page(self.driver)
        login_page.empty_email_registration_attempt(self.driver)
        self.assertTrue(login_page.empty_email_alert_visible(self.driver))

    def test5_back_to_main_page_breadcrumb(self):
        main_page.go_to_login_page(self.driver)
        login_page.back_to_main_page_breadcrumbs(self.driver)
        self.assertTrue(main_page.main_page_content_visible(self.driver))

    def test6_log_out(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        self.assertTrue(my_account_page.my_account_content_visible(self.driver))
        my_account_page.log_out(self.driver)
        self.assertTrue(login_page.login_page_content_visible(self.driver))
