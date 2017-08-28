# -*- coding: UTF-8 -*-
import openpyxl

exl= openpyxl.load_workbook("produceSales.xlsx")
sheet=exl.get_sheet_by_name('Sheet')

for c in range(2,sheet.max_row+1):
    if sheet['A'+str(c)].value == 'Celery':
        sheet['B'+ str(c)] = 1.19
        sheet['D'+str(c)] = 1.19*sheet['C'+str(c)].value
exl.save("update.xlsx")