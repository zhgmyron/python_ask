# -*- coding: UTF-8 -*-

with open("leran_python.txt") as file_object:
    content = file_object.readlines()
print (content)
for line in content:
    print((line.replace('Python','c')).rstrip())


