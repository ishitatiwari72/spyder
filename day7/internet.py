# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:19:22 2019

@author: HP
"""
#to get image
import requests
url=requests.get("https://media2.picsearch.com/is?83qFDEj-dBc0g2ODuAtwDcPO7UiPsF2pAEQmO-kwxfc&height=255")
with open ('comic.png','wb') as f:
    f.write(url.content)
    f.write(url.text)
    
from Bs4 import BeautifulSoup
import requests