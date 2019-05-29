# -*- coding: utf-8 -*-
"""
Created on Sat May 11 06:55:31 2019

@author: HP
"""


"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""

from PIL import Image

i=input("enter image name")
img=Image.open(i)
img_rotate=img.transpose(Image.ROTATE_90)
img_rotate.show()

#crop
crop_img=img.crop(box=(100,100,160,204))
crop_img.save("sample1_crop.jpg")


#thumbnail
img.thumbnail((75,75))
print (img.width,img.height)
img.save("thumbnail_sample.jpg")


#greyscal
img = Image.open(i).convert('L')
img.save('greyscale.jpg')