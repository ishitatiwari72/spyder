# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:52:44 2019

@author: HP
"""

"""
Code Challenge 3

Watermarking Application

Have some pictures you want copyright protected? Add your own logo or text lightly 
across the background so that no one can simply steal your graphics off your site. 
Make a program that will add this watermark to the picture.
"""
image_list=['idimage.png','id_img.png']
img1=[]
from PIL import ImageDraw,ImageFont,Image
def water_mark():
    for img1 in image_list:
        i=Image.open(img1) 
        text="vshanno"
        draw=ImageDraw.Draw(i)
        fnt=ImageFont.truetype('arial.ttf',30)
        #text width and text height
        txt_w,txt_h=draw.textsize(text,fnt)
        print("tw="+str(txt_w)+"txt_h"+str(txt_h))
        draw.text((150,250),text,font=fnt)
        i.save(i)
    return img1