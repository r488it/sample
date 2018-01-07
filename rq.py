# -*- coding: UTF-8 -*-
from PIL import Image
import fastzbarlight
import argparse
import requests
import cv2
import numpy as np
import os
import shutil

def check_rm(cut_f,x=1,y=1):

	img = cv2.imread(cut_f)
	pixelValue = img[x, y]

	if pixelValue[0] == 0 and pixelValue[1] == 213 and pixelValue[2] == 255 :
		shutil.move(cut_f,"image/cut/y/")
	elif pixelValue[0] == 96 and pixelValue[1] == 158 and pixelValue[2] == 0 :
		shutil.move(cut_f,"image/cut/g/")
	elif pixelValue[0] == 58 and pixelValue[1] == 30 and pixelValue[2] == 196 :
		shutil.move(cut_f,"image/cut/r/")
	elif pixelValue[0] == 0 and pixelValue[1] == 88 and pixelValue[2] == 255 :
		shutil.move(cut_f,"image/cut/o/")
	elif pixelValue[0] == 255 and pixelValue[1] == 255 and pixelValue[2] == 255 :
		shutil.move(cut_f,"image/cut/w/")
	elif pixelValue[0] == 186 and pixelValue[1] == 81 and pixelValue[2] == 0 :
		shutil.move(cut_f,"image/cut/b/")
	elif pixelValue[0] == 0 and pixelValue[1] == 0 and pixelValue[2] == 0:
		check_rm(cut_f,x+10,y+10)
	else:
		print(cut_f)
		# os.remove(cut_f)

def clf(fopath):
	top = fopath
	for root, dirs, files in os.walk(top, topdown=False):
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

def cut(name):
	list = []
	img = cv2.imread("image/test"+ str(name) +".png")
	height, width, channels = img.shape

	height_split = 3
	width_split = 3
	new_img_height = int(height / height_split)
	new_img_width = int(width / width_split)

	for h in range(height_split):
		height_start = h * new_img_height
		height_end = height_start + new_img_height

		for w in range(width_split):
			width_start = w * new_img_width
			width_end = width_start + new_img_width

			file_name = "image/cut/test" + str(name) + "-" +  str(h) + "-" + str(w) + ".png"
			clp = img[height_start:height_end, width_start:width_end]
			cv2.imwrite(file_name, clp)
			list.append("image/cut/test" + str(name) + "-" +  str(h) + "-" + str(w) + ".png")
	return list

def encodeqr(name):
	with open("image/test"+ str(name) +".png", 'rb') as img_file:
		image = Image.open(img_file)
		image.load()

	codes = fastzbarlight.scan_codes('qrcode', image)
	print(codes)
	return codes

def save_image(name,image):
	fname = "image/test"+ str(name) + ".png"
	with open(fname, "wb") as fout:
		fout.write(image)
	# img = cv2.imread(fname)
	# dst = img[24:222, 24:222]
	# cv2.imwrite(fname, dst)


def getpnglist(url):
	r = requests.get(url)
	res = r.content.decode('utf-8').split('"')
	list = []
	for i in range(len(res)):
		if "png" in res[i]:
			print("http://qubicrube.pwn.seccon.jp:33654" + res[i])
			list.append("http://qubicrube.pwn.seccon.jp:33654" + res[i])
	return list


def getpng(url):
	r = requests.get(url)
	img_file = r.content
	return img_file


while 1:

	print("input url:   ",end="")
	url = input()
	# print(list)
	if url == "":
		ans = encodeqr(6)
		if ans == None:
			print("Noce")
		else:
			list = getpnglist(ans[0].decode('utf-8'))
			for i in range(len(list)):
				if "qubicrube" in list[i]:
					img_file = getpng(list[i])
					save_image(i,img_file)
					cutlist = cut(i)
					for j in range(len(cutlist)):
						check_rm(cutlist[j])
					encodeqr(i)
	else:
		clf("image/cut/b/")
		clf("image/cut/g/")
		clf("image/cut/o/")
		clf("image/cut/r/")
		clf("image/cut/w/")
		clf("image/cut/y/")
		list = getpnglist(url)
		for i in range(len(list)):
			img_file = getpng(list[i])
			save_image(i,img_file)
			cutlist = cut(i)
			for j in range(len(cutlist)):
				check_rm(cutlist[j])
			encodeqr(i)

# while 1:
# 	print("input url:   ",end="")
# 	url = input()
# 	getpng(url)


#3 http://qubicrube.pwn.seccon.jp:33654/04c0348a6aeca46e33af
#4 http://qubicrube.pwn.seccon.jp:33654/05778a23f9eca28ff7e2
#5 http://qubicrube.pwn.seccon.jp:33654/066a75f5d4895eb1d668
#6 http://qubicrube.pwn.seccon.jp:33654/07f06a3ec2039c403953
#7 http://qubicrube.pwn.seccon.jp:33654/08dbdb72757675be6bf6
#8 http://qubicrube.pwn.seccon.jp:33654/099ee1d7a7ae204f284d
#9 http://qubicrube.pwn.seccon.jp:33654/105019f4e43866e664e2
#10 http://qubicrube.pwn.seccon.jp:33654/11ed5b705e72e9fa2e57

