import unittest
from selenium import webdriver
from config import test_settings


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(test_settings.page_url)

    def tearDown(self):
        self.driver.quit()
