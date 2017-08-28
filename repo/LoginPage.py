# -*- coding: UTF-8 -*-
from BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    usename=(By.NAME,'retailerUsername')
    password=(By.NAME,'password')
    button =(By.CSS_SELECTOR,"div.form-group > button")
    logo = (By.CLASS_NAME,"loginLogo")

    def set_username(self,username):
        name=self.driver.find_element(*LoginPage.usename)
        name.clear()
        name.send_keys(username)
    def set_password(self,password):
        pwd=self.driver.find_element(*LoginPage.password)
        pwd.clear()
        pwd.send_keys(password)
    def click_submit(self):
        submitbtn=self.driver.find_element(*LoginPage.button)
        submitbtn.click()

    def after_login(self):
        gusername = self.driver.find_element(*LoginPage.logo)
        return gusername.get_attribute('title')
class Accountpage(BasePage):
    pass

class CouponPage(LoginPage):
    addbutton=(By.ID,'addCoupon')
    title=(By.ID,'editTitle')
    description=(By.ID,'editDescription')
    code =(By.ID,'editCode')
    link=(By.ID,'editLinkUrl')
    startdate=(By.ID,'editStartDate')
    enddate=(By.ID,'editEndDate')
    categoryid=(By.ID,'editCategoryIDs')
    productid=(By.ID,'editProductIDs')
    submitbutton=(By.ID,'editSubmit')

    def add_button(self):
        addbutton= self.driver.find_element(*CouponPage.add_button)
        addbutton.click()
    def add_title(self,title):
        addtitle= self.driver.find_element(*CouponPage.title)
        addtitle.clear()
        addtitle.send_keys(title)
    def add_description(self,desc):
        adddesc= self.driver.find_element(*CouponPage.description)
        adddesc.clear()
        adddesc.send_keys(desc)
    def add_code(self,code):
        adddcode= self.driver.find_element(*CouponPage.code)
        adddcode.clear()
        adddcode.send_keys(code)
    def add_link(self,link):
        addlink= self.driver.find_element(*CouponPage.link)
        addlink.clear()
        addlink.send_keys(link)
    def add_startdate(self,startdate):
        addsdatec= self.driver.find_element(*CouponPage.startdate)
        addsdatec.clear()
        addsdatec.send_keys(startdate)
    def add_enddate(self,enddate):
        addedatec= self.driver.find_element(*CouponPage.enddate)
        addedatec.clear()
        addedatec.send_keys(enddate)
    def click_submit(self):
        submitbtn=self.driver.find_element(*CouponPage.submitbutton)
        submitbtn.click()
