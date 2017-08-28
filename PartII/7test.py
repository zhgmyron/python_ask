# -*- coding: UTF-8 -*-
import re
# beginsWithHello = re.compile(r'^Hello')
# a=beginsWithHello.search('Hello world!')
#
#
# endsWithNumber = re.compile(r'\d+$')
# b=endsWithNumber.search('Your number is 42')

a="  hello     "
red= re.compile(r'(([0-9a-zA-Z]+(\s+))*([0-9a-zA-Z]+))')
b= red.search(a)
print (b.group())