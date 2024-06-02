from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


def wait_for_visibility_of_element_id(driver_instance, loc_id, time_to_wait=10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.ID, loc_id)))
    except TimeoutException:
        element = False
    return element


def wait_for_visibility_of_element_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        element = False
    return element


def wait_for_visibility_of_element_classname(driver_instance, classname, time_to_wait=10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, classname)))
    except TimeoutException:
        element = False
    return element


def wait_for_invisibility_of_element_id(driver_instance, loc_id, time_to_wait=10):
    try:
        inv_element = WebDriverWait(driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.ID, loc_id)))
    except TimeoutException:
        inv_element = False
    return inv_element


def wait_for_invisibility_of_element_xpath(driver_instance, xpath, time_to_wait=10):
    try:
        inv_element = WebDriverWait(driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        inv_element = True
    return inv_element


def hoverOverElement(driver_instance, xpath):
    element = driver_instance.find_element("xpath", xpath)
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()