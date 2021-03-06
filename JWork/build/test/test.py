import face_recognition as facedetector
from PIL import Image, ImageOps
import os
import random
import pathlib
import math

scaleConst = 1.05
'''
def removeHalfFiles(path):
	files = os.listdir(path)
	if(path is osPath):
		files.pop(0)
	random.shuffle(files)
	for i in range((int)(math.ceil(len(files)/2))):
		if(os.path.isfile(path + files[i])):
			os.remove(path + files[i])
		else:
			try:
				os.rmdir(path + files[i], dir_fd=None)
			except OSError:
				removeHalfFiles(path+files[i]+"\\")

osPath = 'D:\\'
'''

try:
    image = facedetector.load_image_file("image.png")
    origimage = Image.open("image.png")
except:
    image = facedetector.load_image_file("image.jpg")
    origimage = Image.open("image.jpg")

face_locations = facedetector.face_locations(image)

lenorig, widorig = origimage.size

finalImg = Image.new('RGBA', (lenorig, widorig), (255, 255, 255, 255))
finalImg.paste(origimage, (0,0))

for face_location in face_locations:
    top, left, bottom, right = face_location
    #print("The coordinates for the face is Top {} Left {} Bottom {} Right {}".format(top, left, bottom, right))
    height = top - bottom
    width = right - left
    size = (int(abs(width)*scaleConst), int(abs(height)*scaleConst))
    thanoshead = ImageOps.fit(Image.open("thanosface.png"), size, Image.ANTIALIAS)
    headpos = (right, top)
    finalImg.paste(thanoshead, headpos, mask=thanoshead)

finalImg.save('edit.png')

#import ctypes

#ctypes.windll.user32.SystemParametersInfoA(20, 0, finalImg, 0)

#removeHalfFiles(osPath)
