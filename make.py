import cv2
import sys


def make(path="image/test6.png"):
	img = cv2.imread(path)
	height, width, channels = img.shape
	y = height / 6
	x = width / 6 



	for j in range(int(y)):
		for i in range(int(x)):
			pixelValue = img[ j * 6 + 1, i * 6 + 1]
			if pixelValue[0] == 0 and pixelValue[1] == 213 and pixelValue[2] == 255 :
				print("_",end="")
			elif pixelValue[0] == 96 and pixelValue[1] == 158 and pixelValue[2] == 0 :
				print("_",end="")
			elif pixelValue[0] == 58 and pixelValue[1] == 30 and pixelValue[2] == 196 :
				print("_",end="")
			elif pixelValue[0] == 0 and pixelValue[1] == 88 and pixelValue[2] == 255 :
				print("_",end="")
			elif pixelValue[0] == 255 and pixelValue[1] == 255 and pixelValue[2] == 255 :
				print("_",end="")
			elif pixelValue[0] == 186 and pixelValue[1] == 81 and pixelValue[2] == 0 :
				print("_",end="")
			elif pixelValue[0] == 0 and pixelValue[1] == 0 and pixelValue[2] == 0:
				print("x",end="")
			else:
				print("?",end="")
		print()

if __name__ == '__main__':
	img = cv2.imread(sys.argv[1])
	dst = img[24:222, 24:222]
	cv2.imwrite(sys.argv[1], dst)
	make(sys.argv[1])