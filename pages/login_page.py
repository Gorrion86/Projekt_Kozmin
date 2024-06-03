from helpers.support_functions import *
from selenium.webdriver.common.by import By
from test_data import login_data


class LoginPageLocators:
    customer_login_content = (By.ID, 'customer_login')
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    login_button = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/button')
    register_button = (By.XPATH, '//*[@id="customer_login"]/div[2]/form/p[3]/button')
    wrong_login_alert = (By.XPATH, '//*[@class="woocommerce-error"]/li[contains(.,"nieprawidłowa nazwa użytkownika lub hasło.")]')
    empty_email_registration_alert = (By.XPATH, '//*[@class="woocommerce-error"]/li[contains(.,"Proszę podać poprawny adres e-mail.")]')
    breadcrumb_main_page = (By.XPATH, '//*[@class="woocommerce-breadcrumb"]/a[contains(.,"Strona główna")]')


def login_page_content_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, LoginPageLocators.customer_login_content)
    return element.is_displayed()


def correct_login(driver_instance):
    wait_for_visibility_of_element(driver_instance, LoginPageLocators.username)
    driver_instance.find_element(*LoginPageLocators.username).send_keys(login_data.correct_username)
    driver_instance.find_element(*LoginPageLocators.password).send_keys(login_data.correct_password)
    driver_instance.find_element(*LoginPageLocators.login_button).click()


def incorrect_login(driver_instance):
    wait_for_visibility_of_element(driver_instance, LoginPageLocators.username)
    driver_instance.find_element(*LoginPageLocators.username).send_keys(login_data.incorrect_username)
    driver_instance.find_element(*LoginPageLocators.password).send_keys(login_data.incorrect_password)
    driver_instance.find_element(*LoginPageLocators.login_button).click()


def wrong_login_alert_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, LoginPageLocators.wrong_login_alert)
    return element.is_displayed()


def empty_email_registration_attempt(driver_instance):
    wait_for_visibility_of_element(driver_instance, LoginPageLocators.register_button)
    driver_instance.find_element(*LoginPageLocators.register_button).click()


def empty_email_alert_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, LoginPageLocators.empty_email_registration_alert)
    return element.is_displayed()


def back_to_main_page_breadcrumbs(driver_instance):
    wait_for_visibility_of_element(driver_instance, LoginPageLocators.breadcrumb_main_page)
    driver_instance.find_element(*LoginPageLocators.breadcrumb_main_page).click()