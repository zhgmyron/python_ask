# -*- coding: UTF-8 -*-
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(datas):
    colWidths =[0] * len(tableData)

    a= len(datas)
    b= len(datas[0])
    for i in range(a):
        for j in range(b):
            if len(datas[i][j])>colWidths[i]:
                colWidths[i] = len(datas[i][j])

    for i in range(b):
        for j in range(a):
            print (tableData[j][i].ljust(colWidths[j]),end=' ')
        print('')

printTable(tableData)
