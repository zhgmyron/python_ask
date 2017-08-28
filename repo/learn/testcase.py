# -*- coding: UTF-8 -*-
import os,sys
sourcepath=sys.path[0]+"\\test_case\\"
caselist=os.listdir(sourcepath)
print(caselist)
for a in caselist:
    s=a.split('.')[1]
    if s=='py':
        os. system('sourcepath %s 1>>log.txt 2>&1'%a)