from selenium.webdriver.common.by import By
from helpers.support_functions import *
from test_data import login_data
from time import sleep

customer_login_content_id = "customer_login"
username_id = "username"
password_id = "password"
rememberme_checkbox_id = "rememberme"
login_button_xp = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
login_error_alert_xp = '//*[@id="content"]/div/div[1]/ul'


def login_page_content_visible(driver_instance):
    element = wait_for_visibility_of_element_by_id(driver_instance, customer_login_content_id)
    return element.is_displayed()


def correct_login(driver_instance):
    driver_instance.find_element(By.ID, username_id).send_keys(login_data.correct_username)
    driver_instance.find_element(By.ID, password_id).send_keys(login_data.correct_password)
    driver_instance.find_element(By.XPATH, login_button_xp).click()


def incorrect_login(driver_instance):
    driver_instance.find_element(By.ID, username_id).send_keys(login_data.incorrect_username)
    driver_instance.find_element(By.ID, password_id).send_keys(login_data.incorrect_password)
    driver_instance.find_element(By.XPATH, login_button_xp).click()


def login_error_visible(driver_instance):
    element = wait_for_visibility_of_element_by_xpath(driver_instance, login_error_alert_xp)
    return element.is_displayed()
