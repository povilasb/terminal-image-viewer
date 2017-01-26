#!/usr/bin/python
"""
@@Author: Deniz Rasim Uluğ
@@Version: 1.0
"""


from PIL import Image
from math import ceil
import color_table
import sys

crop_size=50
file_name="image.jpg"
if len(sys.argv)>1:
	file_name = sys.argv[1]

if len(sys.argv)>2:
	crop_size=int(sys.argv[2])

im = Image.open(file_name)
#Currently not used
def reduce_array(liste,n,w,h):

	lengthi = len(liste)
	lengthj = len(liste[0])
	i=0
	while(i<lengthi-1):
		j=0
		while(j<lengthj-1):
			liste[i][j][:] = [x / (n*n) for x in liste[i][j]]
			j+=1
		i+=1
	w=w%n if w%n!=0 else n
	h=h%n if w%n!=0 else n
	i=0
	while(i<lengthi-1):
		#liste[i][-1]/=w*n
		liste[i][-1][:] = [x / (w*n) for x in liste[i][-1]]
		i+=1
	j=0
	while(j<lengthj-1):
		#liste[-1][j]/=h*n
		liste[-1][j][:] = [x / (h*n) for x in liste[-1][j]]
		j+=1
	#liste[-1][-1] = w*h
	liste[-1][-1][:] = [x / (n*n) for x in liste[-1][-1]]

#Currently not used
def find_index(x,n):
	retval=0
	value = n
	while(1):
		if value>=x:
			return retval
		retval+=1
		value+=n

#return the average RGB of a region as a tuple
def average_rgb(array):
	n=0
	retval=[0,0,0]
	i=0
	while(i<len(array)):
		#print(array[i])
		n += array[i][0]
		retval[0] += array[i][0] * array[i][1][0] 
		retval[1] += array[i][0] * array[i][1][1] 
		retval[2] += array[i][0] * array[i][1][2] 
		i+=1
	
	retval[0]//=n
	retval[1]//=n
	retval[2]//=n
	#print(tuple(retval))
	return tuple(retval)

#Fill's the output array given an image in cropsizeXcropsize squares
def fill_rgb_array(image,liste,crop_size):
	image_size = image.size[0]*image.size[1]
	i=0 
	while(i<height):
		j = (i+crop_size) if (i+crop_size)<height else height
		
		k=0
		while(k<width):
			l = (k+crop_size) if (k+crop_size)<width else width

			bom=image.crop((k,i,l,j))

			liste[i//crop_size][k//crop_size] = average_rgb(bom.getcolors( image_size ))

			k=l

		i=j

def rgb2hex(rgb):  
	hexx= '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])  
	return  int(color_table.rgb2short(hexx)[0])

width, height = im.size

#Array to hold average RGB values
rgb_array = [ [[0,0,0]]*ceil(width/crop_size) for _ in range(ceil(height/crop_size))] 

fill_rgb_array(im,rgb_array,crop_size)

#Print a blank space in average RGB for each square in picture
i=0
while(i<len(rgb_array)):
	j=0
	while(j<len(rgb_array[i])):
		hexx = rgb2hex(rgb_array[i][j])
		sys.stdout.write('\033[48;5;%sm ' % (hexx) + "\033[0m" )
		j+=1
	print("")
	i+=1










