from tests.base_test import BaseTest
from pages import main_page


class MainPageTest(BaseTest):

    def test1_main_page_logo_visible(self):
        self.assertTrue(main_page.logo_visible(self.driver))

    def test2_main_page_popup_dismiss(self):
        self.assertTrue(main_page.popup_visible(self.driver))
        main_page.popup_dismiss(self.driver)
        self.assertFalse(main_page.popup_invisible(self.driver))
