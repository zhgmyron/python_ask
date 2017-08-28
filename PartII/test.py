# -*- coding: UTF-8 -*-
import os
from urllib.request import urlretrieve
comicUrl='http://imgs.xkcd.com/comics/borrow_your_laptop.png'
urlretrieve(comicUrl,os.path.basename(comicUrl))
