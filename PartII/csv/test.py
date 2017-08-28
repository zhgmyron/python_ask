# -*- coding: UTF-8 -*-
import csv

file= open('example.csv')
page=csv.reader(file)
print(list(page))