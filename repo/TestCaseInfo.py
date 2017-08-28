# -*- coding: UTF-8 -*-
class TestCaseInfo():
    def __init__(self):
        self.id= ""
        self.pwd = 'test'
        self.name = 'netonnet'
        self.baseurl="http://dev.repo.pricerunner.com"
        self.result = ""
        self.errorinfo = ""
        #account
        self.acname='Jimmy Korkeamaa'
        self.acemail='jimmy.korkeamaa@pricerunner.com'
        self.acphone='0729674015'
class Testcoupon():
    def __init__(self):
        self.url=TestCaseInfo().baseurl+"/coupon/list"
        self.title="test"
        self.Description ="test desc"
        self.code="123456"
        self.linkurl="http://baid.com"
        self.startdate="2017-03-16"
        self.enddate="2017-04-26"
