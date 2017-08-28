# -*- coding: UTF-8 -*-
import csv,os

os.mkdir('headerRem',exist_ok=True)

for csvFile in os.listdir('.'):
    if not csvFile.endswith('.csv'):
        continue
    print('Removing header from ' + csvFile + '...')

    csvRows =[]
    csvFileobj


