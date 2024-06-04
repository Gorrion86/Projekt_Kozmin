from tests.base_test import BaseTest
from pages import main_page
from config.test_settings import TestSettings
from time import sleep


class MainPageTest(BaseTest):

    def test1_logo_visible(self):
        self.assertTrue(main_page.logo_visible(self.driver))

    def test2_main_page_content_visible(self):
        self.assertTrue(main_page.main_page_content_visible(self.driver))

    def test3_main_page_popup_dismiss(self):
        self.assertTrue(main_page.popup_visible(self.driver))
        main_page.popup_dismiss_click(self.driver)
        self.assertFalse(main_page.popup_invisible(self.driver))
