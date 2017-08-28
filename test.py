# -*- coding: UTF-8 -*-
def fn(n):
    if n==1 or n==0:
        return 1
    elif n>1:
        return fn(n-1)+ fn(n-2)

print(fn(5))