import cv2
import sys


def make(path):
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

def look(path,x,y):
	img = cv2.imread(path)
	height, width, channels = img.shape
	i = int(x)
	j = int(y)

	print("height={0} width={1} channels={2}".format(height, width, channels))
	print("R={0[0]}({0[0]:X}) G={0[1]}({0[1]:X}) B={0[2]}({0[2]:X})".format(img[i,j]))

if __name__ == '__main__':
	# img = cv2.imread(sys.argv[1])
	# dst = img[24:222, 24:222]
	# cv2.imwrite(sys.argv[1], img)
	look(sys.argv[1],sys.argv[2],sys.argv[3])



