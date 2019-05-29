# -*- coding: utf-8 -*-
"""
Created on Sun May 19 08:46:47 2019

@author: HP
"""
"""
Code Challenge 2

I-Card Generation System
Write a Python code for a system that generates I-card for all studentsof Forsk
Summer Developer Program and store them in image format. 

It must take names and other required information from the user.
"""
from PIL import Image,ImageDraw,ImageFont
j=input("enter your email")
name= input ("enter your name")
roll= input("enter your roll no")
img = Image.new('RGB', (1000, 600), color = (255, 255,255))
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype('arial.ttf',50)
d.text((100,40),"\n GLOBAL TECHNICAL CAMPUS",font=fnt,fill=(0,0,0))
#logopaste
img1=Image.open('gitlogo.png')
offset=(90,150)
img.paste(img1,offset)
fnt = ImageFont.truetype('arial.ttf',35)
d.text((220,150),"GLOBAL INSTITUE OF TECHNOLOGY",font=fnt,fill=(0,0,0))
fnt1= ImageFont.truetype('arial.ttf',23)
d.text((220,190),'E-mail:'+ j +',web:-www.gitjaipur.com',font=fnt1,fill=(0,0,0))
fnt= ImageFont.truetype('arial.ttf',40)
d.text((300,230),"STUDENT ID CARD",font=fnt,fill=(0,0,0))
i= Image.open('idimg1.jpg')
#w,h=i.size() tupple objects are not callable
#print (w,h)
#image of student
i=i.resize((130,200))
offset=(390,280)
img.paste(i,offset)
#logo of nba
img2=Image.open('nba.png')
offset=(150,300)
img.paste(img2,offset)
fnt=ImageFont.truetype('arial.ttf',35)
d.text((350,480),name,font=fnt,fill=(0,0,0))
d.text((350,510),roll,font=fnt,fill=(0,0,0))
d.text((100,540),"Computer Sciencce & Engg.\n2016-2020",font=fnt1,fill=(0,0,0))
d.text((700,565),"Registrar",font=fnt1,fill=(0,0,0))
border_im = Image.new('RGB', (img.width+10, img.height+10),'black')
border_im.paste(img, (5, 5))
border_im.save('id.png')
img.save('id.png')

