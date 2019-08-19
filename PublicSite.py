# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PublicSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_public_site(self):
        driver = self.driver
        driver.get("http://pwssitecore/sitecore/login")
        driver.find_element_by_id("UserName").click()
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("admin")
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("b")
        driver.find_element_by_id("LogInBtn").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Marketing Control Panel'])[1]/following::span[1]").click()
        driver.find_element_by_id("Ribbon110D559FDEA542EA9C1C8A5DF7E70EF9_Nav_PublishStrip").click()
        driver.find_element_by_id("B414550BADAF4542C9ADF44BED5FA6CB3E_menu_button").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Reset Field'])[90]/following::td[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=7 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("NextButton").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
