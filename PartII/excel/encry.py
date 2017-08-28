# -*- coding: UTF-8 -*-
import PyPDF2
pdffile=open('meetingminutes.pdf','rb')
pdfread= PyPDF2.PdfFileReader(pdffile)

pdfwriter =PyPDF2.PdfFileWriter()
for i in range(pdfread.numPages):
    pageobj= pdfread.getPage(i)
    pdfwriter.addPage(pageobj)

pdfwriter.encrypt("hello")
reslutpdf= open("encry.pdf",'wb')
pdfwriter.write(reslutpdf)
reslutpdf.close()