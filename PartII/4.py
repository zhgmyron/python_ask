# -*- coding: UTF-8 -*-
spam = ['apples', 'bananas', 'tofu', 'cats']
def ch(list):
    new=''
    for i in list[:-1]:
        new+= i+','
    new+= 'and '+list[-1]
    return new
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

b= len(grid)
a= len(grid[0])
for c in range(a):
    for m in range(b):
        print(grid[m][c],end='')
    print('')