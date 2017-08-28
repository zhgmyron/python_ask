# -*- coding: UTF-8 -*-
# import webbrowser,sys, pyperclip
# if len(sys.argv) > 1:
#     address =' '.join(sys.argv[1:])
# else:
#     address= pyperclip.paste()
#
# webbrowser.open("https://www.google.com.sg/maps/place/"+ address)
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
playfile = open('Rose.txt',"wb")
for line in res.iter_content(10000):
    playfile.write(line)
playfile.close()