# -*- coding: UTF-8 -*-
import unittest
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def give_raise(self,add=5000):

        return int(self.salary)+add


class Test_employee(unittest.TestCase):
    def setUp(self):
        self.base = Employee("ron","100")


    def test_give_default(self):

        self.assertEqual("5100",str(self.base.give_raise()))



