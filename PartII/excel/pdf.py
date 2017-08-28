# -*- coding: UTF-8 -*-
import PyPDF2

pdfobj= PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))

pdfWriter = PyPDF2.PdfFileWriter()

for num in range(pdfobj.numPages):
    pageobj= pdfobj.getPage(num)
    pdfWriter.addPage(pageobj)
pdfout= open('combine.pdf','wb')
pdfWriter.write(pdfout)
pdfout.close()
