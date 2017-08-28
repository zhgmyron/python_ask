# -*- coding: UTF-8 -*-
import docx
file= open('guests.txt')
filedoc= docx.Document()
for i in file.readlines():
    print(i)
    filedoc.add_paragraph(i)

filedoc.save('update.docx')