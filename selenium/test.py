# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest,time,re
import sys

sys.path.append("\\func")
from func import locator

we =locator
chromedriver ="F:\soft\chromedriver.exe"
dr=webdriver.Chrome(chromedriver)
dr.get('http://www.baidu.com')
#调用封装的方法
we.findId(dr,"kw").send_keys('selenium')
time.sleep(2)
we.findId(dr,"su").click()
time.sleep(2)
dr.quit()


