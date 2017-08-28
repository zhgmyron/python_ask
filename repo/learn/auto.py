# -*- coding: UTF-8 -*-
from learn.widget import Widget
import unittest
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def test_size(self):
        self.assertEqual(self.widget.getSize(),(40,40),"not same")
    def test_resize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.getSize(),(100,500),"not same")
    def tearDown(self):
        self.widget=None
#
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase("test_size"))
#     suite.addTest(WidgetTestCase("test_resize"))
#     return suite

if __name__ == "__main__":
    unittest.main()