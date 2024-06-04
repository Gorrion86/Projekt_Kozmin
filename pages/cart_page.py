from helpers.support_functions import *
from selenium.webdriver.common.by import By


class CartPageLocators:
    cart_h1 = (By.XPATH, '//*[@class="entry-title"][contains(.,"Koszyk")]')
    cart_item = (By.XPATH, '//*[@class="woocommerce-cart-form__cart-item cart_item"]')
    remove_item_button = (By.XPATH, '//*[@class="remove"][1]')
    cart_empty_info = (By.XPATH, '//*[@class="cart-empty woocommerce-info"]')


def cart_h1_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, CartPageLocators.cart_h1)
    return element.is_displayed()


def check_for_product_in_cart(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, CartPageLocators.cart_item)
    return element.is_displayed()


def remove_item_from_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, CartPageLocators.remove_item_button)
    driver_instance.find_element(*CartPageLocators.remove_item_button).click()


def check_if_cart_is_empty(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, CartPageLocators.cart_empty_info)
    return element.is_displayed()
