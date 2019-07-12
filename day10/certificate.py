# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:31:02 2019

@author: HP
"""
"""
Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""
i= input("enter the name")
from PIL import Image,ImageDraw,ImageFont
img = Image.new('RGB', (1000, 600), color = (255, 255,255))
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype('arial.ttf',50)
d.text((190,90),"FORKS TECHNOLOGY\n",font=fnt,fill=(0,0,0))
#d.text((200,100), "\n",font=fnt, fill=(255,255,0))
fnt1 = ImageFont.truetype('arial.ttf',40)
d.text((100,180), "This is to certify that Mr/Miss\n",font=fnt1, fill=(0,0,0))
d.text((620,180),i,font=fnt1,fill=(0,0,0))
d.text((110,230), " had participated in a Python Bootcamp\n",font=fnt1, fill=(0,0,0))
d.text((180,280), " workshop held on 24,May,2019\n",font=fnt1, fill=(0,0,0))
d.text((250,330), "conducted by the Forks\n",font=fnt1, fill=(0,0,0))
d.text((320,380), " Technology. \n",font=fnt1, fill=(0,0,0))
img1=Image.open("sign.png")
offset=(100,400)
img.paste(img1,offset)
#img.save('pil_text.png')
img2=Image.open('seal.png')
offset_=(800,450)
img.paste(img2,offset_)
im3=Image.open('logo.png')
offset_=(800,100)
img.paste(im3,offset_)
border_im = Image.new('RGB', (img.width+20, img.height+20), 'black')
border_im.paste(img, (10, 10))
border_im.save("pil_text.png")
img.save('pil_text.png')







