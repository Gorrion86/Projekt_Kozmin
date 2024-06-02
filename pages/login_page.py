from selenium.webdriver.common.by import By
from helpers.support_functions import *
from test_data import login_data
from time import sleep

customer_login_content_id = "customer_login"
username_id = "username"
password_id = "password"
rememberme_checkbox_id = "rememberme"
login_button_xp = '//*[@id="customer_login"]/div[1]/form/p[3]/button'


def correct_login(driver_instance):
    driver_instance.find_element(By.ID, username_id).send_keys(login_data.proper_username)
    driver_instance.find_element(By.ID, password_id).send_keys(login_data.proper_password)
    driver_instance.find_element(By.XPATH, login_button_xp).click()