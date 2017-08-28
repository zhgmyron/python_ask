# -*- coding: UTF-8 -*-
import random
import logging
logging.disable(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
guess = ''
logging.debug('start of program...')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')

    guess = input()
    logging.debug('start guess(%s)'%(guess))
i = random.randint(0, 1) # 0 is tails, 1 is heads
a=['tails','heads']
toss=a[i]
logging.debug("toss is (%s)"%(toss))
if toss == guess:
    print('You got it!')
    logging.debug("toss is (%s) and guees is(%s)"%(toss,guess))
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug("toss is (%s) and guees is(%s)"%(toss,guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')