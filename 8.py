# -*- coding: UTF-8 -*-
def build_person(first_name, last_name, age=''):

    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
def city_country(city,country):
    print("------------------")

def show_magicians(magicians):
    for magician in magicians:
        print(magician,end=' ')

def make_great():
    a=[]
    for name in names:
        a.append('the great '+ name)
    return a
def make_pizza(*toppings):

    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')