# -*- coding: UTF-8 -*-
from random import randint
x = randint(1,6)

class Die():
    def __init__(self, sides=6):
        self.sides=sides
    def roll_die(self):
        return randint(1,self.sides)
a= Die(10)

print (a.roll_die())