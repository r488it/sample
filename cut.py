import cv2
import sys
import os
import make

def chk(file):
	if os.path.exists(file):
		return file
	else:
		a = file.split("/")[-1]
		file = "image/x/" + a
		return file


path = chk('image/cut/' + sys.argv[1] + "/" + '1.png')
img1 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '2.png')
img2 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '3.png')
img3 = cv2.imread(path)


path = chk('image/cut/' + sys.argv[1] + "/" + '4.png')
img4 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '5.png')
img5 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '6.png')
img6 = cv2.imread(path)


path = chk('image/cut/' + sys.argv[1] + "/" + '7.png')
img7 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '8.png')
img8 = cv2.imread(path)
path = chk('image/cut/' + sys.argv[1] + "/" + '9.png')
img9 = cv2.imread(path)




img123 = cv2.hconcat([img1, img2, img3])
img456 = cv2.hconcat([img4, img5, img6])
img789 = cv2.hconcat([img7, img8, img9])
imgall = cv2.vconcat([img123, img456, img789])

cv2.imwrite('image/test6.png', imgall)
img = cv2.imread('image/test6.png')
dst = img[24:222, 24:222]
cv2.imwrite('image/test6.png', dst)

make.make()