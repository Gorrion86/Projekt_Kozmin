from helpers.support_functions import *
from selenium.webdriver.common.by import By

class MyAccountLocators:
    my_account_header = (By.XPATH, '//*[@id="post-9"]/header/h1')

def my_account_header_visible(driver_instance):
    element = wait_for_visibility_of_element(driver_instance, MyAccountLocators.my_account_header)
    return element.is_displayed()