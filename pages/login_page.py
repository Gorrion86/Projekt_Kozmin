from selenium.webdriver.common.by import By
from helpers.support_functions import wait_for_visibility_of_element_id, wait_for_visibility_of_element_xpath
from test_data import login_data
from time import sleep

customer_login_content = "customer_login"
username = "username"
password = "password"
rememberme_checkbox = "rememberme"
login_button = '//*[@id="customer_login"]/div[1]/form/p[3]/button'


def correct_login(driver_instance):
    driver_instance.find_element(By.ID, username).send_keys(login_data.proper_username)
    driver_instance.find_element(By.ID, password).send_keys(login_data.proper_password)
    driver_instance.find_element(By.XPATH, login_button).click()