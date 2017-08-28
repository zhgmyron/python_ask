# -*- coding: UTF-8 -*-
filename='guest.txt'


while True:
    a=input("please input you name:")
    if a =='q':
        break
    else:
        with open(filename,'a') as fileobject:
            fileobject.write(a+'\n')
