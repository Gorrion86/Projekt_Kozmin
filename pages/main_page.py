from helpers.support_functions import *
from selenium.webdriver.common.by import By


class MainPageLocators:
    logo = (By.CLASS_NAME, 'custom-logo-link')
    main_page_content = (By.CLASS_NAME, 'wp-block-cover')
    popup = (By.XPATH, '/html/body/p')
    popup_dismiss = (By.XPATH, '/html/body/p/a')
    my_account_menu_item = (By.ID, 'menu-item-100')
    cart_menu_item = (By.ID, 'menu-item-99')
    search_field = (By.ID, 'woocommerce-product-search-field-0')


def logo_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MainPageLocators.logo)
    return element.is_displayed()


def main_page_content_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MainPageLocators.main_page_content)
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


def search_for_product(driver_instance, product):
    wait_for_visibility_of_element(driver_instance, MainPageLocators.search_field)
    element = driver_instance.find_element(*MainPageLocators.search_field)
    element.send_keys(product)
    element.submit()


def go_to_cart(driver_instance):
    wait_for_visibility_of_element(driver_instance, MainPageLocators.cart_menu_item)
    driver_instance.find_element(*MainPageLocators.cart_menu_item).click()
