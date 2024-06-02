from selenium.webdriver.common.by import By
from helpers.support_functions import *

my_account_header_xp = '//*[@id="post-9"]/header/h1'

def my_account_header_visible(driver_instance):
    element = wait_for_visibility_of_element_by_xpath(driver_instance, my_account_header_xp)
    return element.is_displayed()