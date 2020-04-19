"""Acceptance tests.

Was going to use pytest, but why add another dependency.
"""

import unittest
from selenium import webdriver
import selenium

from app import app

class AcceptanceTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_false(self):
        assert False
    
    def test_true(self):
        assert True
    
    def _generic_test(self, wdriver):
        with wdriver() as driver:
            driver.get("http://localhost:5000")
            elem1 = driver.find_element_by_name(app.ELEM_NAME)
            assert elem1.text == app.WELCOME_TEXT
            elem2 = driver.find_element_by_name(app.BUTTON_NAME)
            elem2.click()
            driver.find_element_by_name(app.NEW_ELEM_NAME)

    def test_selenium_chrome(self):
        self._generic_test(webdriver.Chrome)

    # mark this as a failure since I'm just going to get chrome going
    @unittest.expectedFailure
    def test_selenium_firefox(self):
        self._generic_test(webdriver.Firefox)
