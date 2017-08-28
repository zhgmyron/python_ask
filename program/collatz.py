# -*- coding: UTF-8 -*-

def collatz(num):
    print (num)
    if num ==1:
        print ('done')

    else:
        if num%2 == 0:
            num = int( num/2)
            return collatz(num)

        else:
            num= 3*num +1
            return collatz(num)
a= input("enter num:")

collatz(int(a))








