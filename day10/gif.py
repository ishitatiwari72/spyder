# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:09:00 2019

@author: HP
"""
"""
Code Challenge 4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""
import os,sys
import datetime
import imageio
from pprint import pprint
import time
e=sys.exit
#for given images
#filename=['jp1.jpg','jp2.jpg']
 
def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
	imageio.mimsave(output_file, images, duration=duration)
#duration=0.2
  
if __name__ == "__main__":
	script = sys.argv.pop(0)
	duration = 0.2 
	filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(".jpg")]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
	
create_gif(filenames, duration)

    
    
