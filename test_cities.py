# -*- coding: UTF-8 -*-
import unittest
from location import place


class Test(unittest.TestCase):

    def test_place(self):
        name= place('santiago','chile')
        self.assertEqual(name,'Santiago Chile')

if __name__ == "__main__":
    unittest.main()