from tests.base_test import BaseTest
from config.test_settings import TestSettings
from pages import main_page, product_page, cart_page
from time import sleep


class ShoppingTest(BaseTest):

    def test1_add_product_to_cart(self):
        main_page.search_for_product(self.driver, TestSettings.product1)
        product_page.add_product_to_cart(self.driver)
        self.assertTrue(product_page.see_cart_message_visible(self.driver))
        main_page.go_to_cart(self.driver)
        self.assertTrue(cart_page.cart_h1_visible(self.driver))
        self.assertTrue(cart_page.check_for_product_in_cart(self.driver))

    def test2_remove_product_from_cart(self):
        main_page.search_for_product(self.driver, TestSettings.product2)
        product_page.add_product_to_cart(self.driver)
        main_page.go_to_cart(self.driver)
        self.assertTrue(cart_page.check_for_product_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_if_cart_is_empty(self.driver))

    def test3_buy_products(self):
        pass
