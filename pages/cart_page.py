from helpers.support_functions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_data.shipping_adress_data import ShippingAdressData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CartPageLocators:
    cart_h1 = (By.XPATH, '//*[@class="entry-title"][contains(.,"Koszyk")]')
    cart_item = (By.XPATH, '//*[@class="woocommerce-cart-form__cart-item cart_item"]')
    remove_item_button = (By.XPATH, '//*[@class="remove"][1]')
    cart_empty_info = (By.XPATH, '//*[@class="cart-empty woocommerce-info"]')
    change_quantity = (By.XPATH, '//*[@aria-label="Ilość produktu"]')
    update_cart = (By.XPATH, '//*[@class="button"][contains(.,"Zaktualizuj koszyk")]')
    update_cart_success_message = (By.XPATH, '//*[@class="woocommerce-message"][contains(.,"Koszyk zaktualizowany.")]')
    calculate_shipping_cost = (By.XPATH, '//*[@class="shipping-calculator-button"][contains(.,"Oblicz koszty wysyłki")]')
    city_field = (By.ID, 'calc_shipping_city')
    postal_code_field = (By.ID, 'calc_shipping_postcode')
    update_shipping_cost = (By.XPATH, '//*[@class="button"][contains(.,"Aktualizuj")]')
    shipping_cost_updated_message = (By.XPATH, '//*[@class="woocommerce-info"][contains(.,"Koszty wysyłki zaktualizowane.")]')
    checkout_button = (By.XPATH, '//*[@class="checkout-button button alt wc-forward"][contains(.,"Przejdź do płatności")]')


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


def change_quantity_of_product_in_cart(driver_instance):
    driver_instance.find_element(*CartPageLocators.change_quantity).send_keys(Keys.DELETE)
    driver_instance.find_element(*CartPageLocators.change_quantity).send_keys(2)
    driver_instance.find_element(*CartPageLocators.update_cart).click()
    wait_for_visibility_of_element(driver_instance, CartPageLocators.update_cart_success_message)


def calculate_shipping_cost(driver_instance):
    driver_instance.find_element(*CartPageLocators.calculate_shipping_cost).click()
    wait_for_visibility_of_element(driver_instance, CartPageLocators.city_field)
    driver_instance.find_element(*CartPageLocators.city_field).send_keys(ShippingAdressData.city)
    driver_instance.find_element(*CartPageLocators.postal_code_field).send_keys(ShippingAdressData.postal_code)
    wait_for_element_to_be_clickable(driver_instance, CartPageLocators.update_shipping_cost)
    driver_instance.find_element(*CartPageLocators.update_shipping_cost).click()
    wait_for_visibility_of_element(driver_instance, CartPageLocators.update_cart_success_message)


def checkout_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, CartPageLocators.checkout_button)
    driver_instance.find_element(*CartPageLocators.checkout_button).click()
