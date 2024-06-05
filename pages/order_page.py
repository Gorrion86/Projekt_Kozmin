from helpers.support_functions import *
from selenium.webdriver.common.by import By

class OrderPageLocators:
    first_name = (By.ID, 'billing_first_name')
    last_name = (By.ID, 'billing_last_name')
    street = (By.ID, 'billing_address_1')
    phone = (By.ID, 'billing_phone')
    email = (By.ID, 'billing_email')