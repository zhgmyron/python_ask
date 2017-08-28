# -*- coding: UTF-8 -*-
import unittest
import time
from LoginPage import LoginPage,CouponPage
from selenium import webdriver
from TestCaseInfo import Testcoupon,TestCaseInfo

class Test_Login(unittest.TestCase):
    def setUp(self):
        chromedriver ="F:\soft\chromedriver.exe"
        self.driver=webdriver.Chrome(chromedriver)
        self.testcaseinfo= TestCaseInfo()
        self.testcoupon= Testcoupon()

    def test_login(self):
        try:
            self.driver.get(self.testcaseinfo.baseurl)
            login_page=LoginPage(self.driver)
            login_page.set_username(self.testcaseinfo.name)
            login_page.set_password(self.testcaseinfo.pwd)
            login_page.click_submit()
            time.sleep(2)
            retail_name=login_page.after_login()
            self.assertEqual(self.testcaseinfo.name.lower(),retail_name.lower(),"Not equal")

        except Exception as err:
            self.testcaseinfo.errorinfo= str(err)

    def test_coupon(self):
        try:
            self.test_login()
            self.driver.get(self.testcoupon.url)

            coupon_Page=CouponPage(self.driver)
            time.sleep(3)
            coupon_Page.addbutton()
            coupon_Page.add_title(self.testcoupon.title)
            coupon_Page.add_description(self.testcoupon.Description)
            coupon_Page.add_code(self.testcoupon.code)
            coupon_Page.add_link(self.testcoupon.linkurl)
            coupon_Page.add_startdate(self.testcoupon.startdate)
            coupon_Page.add_enddate(self.testcoupon.enddate)
            coupon_Page.click_submit()


        except Exception as err:
            self.testcaseinfo.errorinfo= str(err)
            print(self.testcaseinfo.errorinfo)
    # def tearDown(self):
    #     self.driver.quit()
# if __name__ == "__main__":
#     unittest.main()

