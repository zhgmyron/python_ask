# -*- coding: UTF-8 -*-
class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type= cuisine_type
        self.number_served= 0
    def describe_restaurant(self):
        print("name: "+self.restaurant_name)
        print("type: "+ self.cuisine_type)

    def open_restaurant(self):
        print("type: "+ self.cuisine_type)

    def set_number_served(self,num):
        if num > 0:
            self.number_served = num
        else:
            print ("you enter a wrong num: " +num)

    def increment_number(self, num):
        self.number_served += num
    def print_num(self):
        print ("number of user to eat: "+ str(self.number_served))

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors =['ice','bar']

    def show(self):

        print (self.flavors)


