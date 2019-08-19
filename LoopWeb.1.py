#!/usr/bin/python

import webbrowser
from time import sleep
import os
from selenium import webdriver
a=0

#while True:
    # webbrowser.open_new("http://google.com")
    # sleep(15)
    # os.system("killall 'Google Chrome'")
    # a=a+0


while True:
 self.driver = webdriver.Chrome()
 self.driver.implicitly_wait(30)
 self.driver.get("http://example.com")
 button = driver.find_element_by_id('buttonID')
 button.click()