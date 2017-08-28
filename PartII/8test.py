# -*- coding: UTF-8 -*-
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
with open('mycat.py','w') as fileobj:
    fileobj.write('cat =' + pprint.pformat(cats) + '\n')
fileobj.close()
# helloFile = open('ha.txt')
# helloContent = helloFile.readlines()
# print (helloContent)