"""Acceptance tests.

Was going to use pytest, but why add another dependency.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium

from app import app

class AcceptanceTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_false(self):
        assert False

    def test_true(self):
        assert True

    def _generic_test(self, driver):
        driver.get("http://localhost:5000")
        elem1 = driver.find_element_by_name(app.ELEM_NAME)
        assert elem1.text == app.WELCOME_TEXT
        elem2 = driver.find_element_by_name(app.BUTTON_NAME)
        elem2.click()
        elem3 = driver.find_element_by_name(app.NEW_ELEM_NAME)
        assert elem3.text == app.NEW_TEXT

    def test_selenium_chrome(self):
        with webdriver.Chrome() as driver:
            self._generic_test(driver)

    def test_selenium_firefox(self):
        firefox_options = FOptions()
        firefox_options.add_argument("--headless")
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        with webdriver.Firefox(options=firefox_options, capabilities=cap) as driver:
            self._generic_test(driver)
