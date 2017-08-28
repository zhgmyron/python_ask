# -*- coding: UTF-8 -*-
import re,pyperclip
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first 3 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''([0-9a-zA-Z.%]+@[0-9a-zA-Z.-]+(\.[a-zA-Z]{2,4}))''')


text= str(pyperclip.paste())
matches=[]

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in phoneRegex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phonenum +=groups[8]
    matches.append(phonenum)

if len(matches) > 0:

    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')