from helpers.support_functions import *
from selenium.webdriver.common.by import By
from test_data.shipping_adress_data import ShippingAdressData
from time import sleep

class OrderPageLocators:
    first_name = (By.ID, 'billing_first_name')
    last_name = (By.ID, 'billing_last_name')
    street = (By.ID, 'billing_address_1')
    phone = (By.ID, 'billing_phone')
    place_order_button = (By.ID, 'place_order')
    form_error_message = (By.XPATH, '//*[@class="woocommerce-error"]')
    order_completed_h1 = (By.XPATH, '//*[@class="entry-title"][contains(.,"Zamówienie otrzymane")]')


def fill_order_form(driver_instance):
    wait_for_visibility_of_element(driver_instance, OrderPageLocators.first_name)
    driver_instance.find_element(*OrderPageLocators.first_name).send_keys(ShippingAdressData.first_name)
    driver_instance.find_element(*OrderPageLocators.last_name).send_keys(ShippingAdressData.last_name)
    driver_instance.find_element(*OrderPageLocators.street).send_keys(ShippingAdressData.street)
    driver_instance.find_element(*OrderPageLocators.phone).send_keys(ShippingAdressData.phone)


def place_order(driver_instance):
    wait_for_visibility_of_element(driver_instance, OrderPageLocators.place_order_button)
    driver_instance.find_element(*OrderPageLocators.place_order_button).submit()


def check_if_order_is_completed(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, OrderPageLocators.order_completed_h1)
    return element.is_displayed()
