from helpers.support_functions import *
from selenium.webdriver.common.by import By
from pages.login_page import LoginPageLocators


class MyAccountLocators:
    my_account_content = (By.XPATH, '//*[@class="woocommerce-MyAccount-content"]')
    logout_button = (By.XPATH, '//*[@class="woocommerce-MyAccount-content"]/p/a[contains(.,"Wyloguj się")]')


def my_account_content_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MyAccountLocators.my_account_content)
    return element.is_displayed()


def log_out(driver_instance):
    wait_for_visibility_of_element(driver_instance, MyAccountLocators.logout_button)
    driver_instance.find_element(*MyAccountLocators.logout_button).click()
    wait_for_visibility_of_element(driver_instance, LoginPageLocators.username)

