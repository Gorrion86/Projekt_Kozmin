from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def wait_for_visibility_of_element(driver_instance, locator, time_to_wait=10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        element = False
    return element


def wait_for_invisibility_of_element(driver_instance, locator, time_to_wait=10):
    try:
        inv_element = WebDriverWait(driver_instance, time_to_wait).until(EC.invisibility_of_element_located(locator))
    except TimeoutException:
        inv_element = False
    return inv_element
