# -*- coding: UTF-8 -*-
prompt = "\nPlease enter the age:"
prompt += "\n(Enter 'quit' when you are finished.) "

active=True
while active == True:

    age=input(prompt)

    if age != 'quit':
        if int(age)<3:
            print("free")
        if int(age) < 12:
            print(10)
        elif int(age) >=12:
            print (15)
    else:
        active=False