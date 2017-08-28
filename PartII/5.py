# -*- coding: UTF-8 -*-
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count={}

for character in message:
    count.setdefault(character,0)

    count[character]=count[character] +1

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn ='X'
for i in range(9):
    printBoard(theBoard)
