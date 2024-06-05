from tests.base_test import BaseTest
from test_data.products_data import ProductsData
from pages import main_page, login_page, product_page, cart_page, order_page
from time import sleep


class ShoppingTest(BaseTest):

    def test1_add_product_to_cart(self):
        main_page.search_for_product(self.driver, ProductsData.product1)
        product_page.add_product_to_cart(self.driver)
        self.assertTrue(product_page.see_cart_message_visible(self.driver))
        main_page.go_to_cart(self.driver)
        self.assertTrue(cart_page.cart_h1_visible(self.driver))
        self.assertTrue(cart_page.check_for_product_in_cart(self.driver))

    def test2_remove_product_from_cart(self):
        main_page.search_for_product(self.driver, ProductsData.product2)
        product_page.add_product_to_cart(self.driver)
        main_page.go_to_cart(self.driver)
        self.assertTrue(cart_page.check_for_product_in_cart(self.driver))
        cart_page.remove_item_from_cart(self.driver)
        self.assertTrue(cart_page.check_if_cart_is_empty(self.driver))

    def test3_buy_products(self):
        main_page.go_to_login_page(self.driver)
        login_page.correct_login(self.driver)
        main_page.search_for_product(self.driver, ProductsData.product1)
        product_page.add_product_to_cart(self.driver)
        main_page.go_to_cart(self.driver)
        cart_page.change_quantity_of_product_in_cart(self.driver)
        main_page.search_for_product(self.driver, ProductsData.product2)
        product_page.add_product_to_cart(self.driver)
        main_page.go_to_cart(self.driver)
        cart_page.calculate_shipping_cost(self.driver)
        cart_page.checkout_cart(self.driver)
        order_page.fill_order_form(self.driver)
        order_page.place_order(self.driver)
        self.assertTrue(order_page.check_if_order_is_completed(self.driver))
