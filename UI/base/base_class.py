import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseClass(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://allegro.pl")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def wait_element_to_be_clickable(self, xpath, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def wait_element_to_be_visible(self, xpath, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element = self.driver.find_element_by_xpath(xpath)
        return element
