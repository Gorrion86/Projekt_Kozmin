from helpers.support_functions import *
from selenium.webdriver.common.by import By
from test_data import login_data

class LoginPageLocators:
    customer_login_content = (By.ID, "customer_login")
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
    login_error_alert = (By.XPATH, '//*[@id="content"]/div/div[1]/ul')


def login_page_content_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, LoginPageLocators.customer_login_content)
    return element.is_displayed()


def correct_login(driver_instance):
    driver_instance.find_element(*LoginPageLocators.username).send_keys(login_data.correct_username)
    driver_instance.find_element(*LoginPageLocators.password).send_keys(login_data.correct_password)
    driver_instance.find_element(*LoginPageLocators.login_button).click()


def incorrect_login(driver_instance):
    driver_instance.find_element(*LoginPageLocators.username).send_keys(login_data.incorrect_username)
    driver_instance.find_element(*LoginPageLocators.password).send_keys(login_data.incorrect_password)
    driver_instance.find_element(*LoginPageLocators.login_button).click()


def login_error_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, LoginPageLocators.login_error_alert)
    return element.is_displayed()
