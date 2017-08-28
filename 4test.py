# -*- coding: UTF-8 -*-
suqares=[]
for i in range(1,11):
    suqares.append(i**2)

favorite=['pizza', 'falafel', 'carrot cake', 'ice cream']
print(favorite[:3])
print(favorite[-3:])
friend=favorite[:]
print(friend)

foods=('chicken','fish','meat','fruit')
print([food for food in foods])

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if ('mushrooms' in requested_toppings ):
    print('true')