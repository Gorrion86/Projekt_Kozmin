from helpers.support_functions import *
from selenium.webdriver.common.by import By

class MainPageLocators:
    logo = (By.CLASS_NAME, "custom-logo-link")
    popup = (By.XPATH, '/html/body/p')
    popup_dismiss = (By.XPATH, '/html/body/p/a')
    my_account_menu_item = (By.ID, "menu-item-100")
    cart_menu_item = (By.ID, "menu-item-99")


def logo_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MainPageLocators.logo)
    return element.is_displayed()


def popup_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MainPageLocators.popup)
    return element.is_displayed()


def popup_invisible(driver_instance):
    element = wait_for_invisibility_of_element(driver_instance, MainPageLocators.popup)
    return element.is_displayed()


def popup_dismiss_click(driver_instance):
    wait_for_visibility_of_element(driver_instance, MainPageLocators.popup_dismiss)
    driver_instance.find_element(*MainPageLocators.popup_dismiss).click()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element(driver_instance, MainPageLocators.my_account_menu_item)
    driver_instance.find_element(*MainPageLocators.my_account_menu_item).click()