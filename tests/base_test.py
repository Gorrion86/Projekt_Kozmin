import unittest
from selenium import webdriver
from config.test_settings import TestSettings


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(TestSettings.page_url)

    def tearDown(self):
        self.driver.quit()
