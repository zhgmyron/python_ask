# -*- coding: UTF-8 -*-
import unittest
import requests

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'
        self.auth=('myron','cool1204')

    def tearDown(self):
        print(self.result)
    def test_user1(self):
        r= requests.get(self.base_url+'/1/',auth=self.auth)
        self.result=r.json()
        self.assertEqual(self.result['username'],'myron')
        self.assertEqual(self.result['email'],'ron.zhao@pricerunner.com')
    def test_user2(self):
        r= requests.get(self.base_url+'/2/',auth=self.auth)
        self.result=r.json()
        self.assertEqual(self.result['username'],'jack')
        self.assertEqual(self.result['email'],'zhgjames@sina.com')

class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('myron','cool1204')

    def tearDown(self):
        print(self.result)
    def test_group1(self):
        r= requests.get(self.base_url+'/1/',auth=self.auth)
        self.result=r.json()
        self.assertEqual(self.result['name'],'tom')