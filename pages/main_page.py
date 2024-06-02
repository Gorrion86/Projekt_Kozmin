from helpers.support_functions import *
from selenium.webdriver.common.by import By

logo_classname = "custom-logo-link"
popup_xp = '/html/body/p'
popup_dismiss_xp = '/html/body/p/a'
my_account_menu_item_id = "menu-item-100"
cart_menu_item = "menu-item-99"


def logo_visible(driver_instance):
    element = wait_for_visibility_of_element_by_classname(driver_instance, logo_classname)
    return element.is_displayed()


def popup_visible(driver_instance):
    element = wait_for_visibility_of_element_by_xpath(driver_instance, popup_xp)
    return element.is_displayed()


def popup_invisible(driver_instance):
    element = wait_for_invisibility_of_element_by_xpath(driver_instance, popup_xp)
    return element.is_displayed()


def popup_dismiss(driver_instance):
    wait_for_visibility_of_element_by_xpath(driver_instance, popup_dismiss_xp)
    driver_instance.find_element(By.XPATH, popup_dismiss_xp).click()


def go_to_login_page(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, my_account_menu_item_id)
    driver_instance.find_element(By.ID, my_account_menu_item_id).click()