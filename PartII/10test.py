# -*- coding: UTF-8 -*-
# def spam():
#     bacon()
# def bacon():
#     raise Exception('This is the error message.')
# spam()
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n ):
        total *= (i+1)
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total
logging.disable(logging.DEBUG)
print(factorial(5))
logging.debug('End of program')

print('Enter the first number to add:')
first =int(input())
print('Enter the second number to add:')
second = int(input())
print('Enter the third number to add:')
third = int(input())
m=(first + second + third)
print('The sum is: ' + str(m))

# import logging
# logging.basicConfig(filename="",level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')
#
