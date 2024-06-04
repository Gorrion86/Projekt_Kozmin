from helpers.support_functions import *
from selenium.webdriver.common.by import By
from time import sleep


class ProductPageLocators:
    add_to_cart = (By.XPATH, '//*[@name="add-to-cart"]')
    see_cart = (By.XPATH, '//*[@class="woocommerce-message"][contains(.,"Zobacz koszyk")]')


def add_product_to_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, ProductPageLocators.add_to_cart)
    driver_instance.find_element(*ProductPageLocators.add_to_cart).click()


def see_cart_message_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, ProductPageLocators.see_cart)
    return element.is_displayed()