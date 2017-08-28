# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

broswer = webdriver.Chrome('F:\soft\chromedriver.exe')
broswer.get("https://gabrielecirulli.github.io/2048/")
broswer.get("https://www.nostarch.com/")
broswer.back()
htmlElem = broswer.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
# #broswer.get("https://gabrielecirulli.github.io/2048/")
# broswer.get("https://gabrielecirulli.github.io/2048/")
#
# broswer.find_element_by_class_name("restart-button").click()
# operate= broswer.find_element_by_class_name('grid-container')
# operate.send_keys(Keys.DOWN)