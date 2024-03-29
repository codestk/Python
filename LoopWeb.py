# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re
from time import sleep


class LoopWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "https://www.katalon.com/"
        #self.verificationErrors = []
        #self.accept_next_alert = True

    def test_loop_web(self):
        for x in range(11):
            driver = self.driver
            driver.get("http://www.queengallery.org/refer.html")
            #driver.get("http://sitecoredevtest0001.azurewebsites.net/refer.html")
            #driver.get("http://www.sitecorethai.com/refer.html")
            #driver.get("http://www.javascriptthai.com/refer.html")
            driver.find_element_by_link_text("StarBug").click()
            sleep(5)
            #driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='DISCOUNT-ON-EVERY-ORDER'])[2]/following::img[1]").click()
            driver.delete_all_cookies()
            sleep(5)
           
            # driver.close()
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
