# -*- coding: UTF-8 -*-
import csv
import os
def open_file(filename):
    with open(filename,'r') as csvfile:
        reader= csvfile.readlines()

    return reader
# def get_string(lines):
#     file_string =''
#     for line in lines:
#         file_string += str(line)
#     return  file_string

def export_different(a,b):
    num=0
    for line in a:

        if line not in b:
            with open("not_in_b.txt",'a') as f:
                f.write(line)
        num+=1
    print(num)
a = open_file("F:\\Appium\\a.txt")
b= open_file("F:\\Appium\\b.txt")

export_different(a,b)



