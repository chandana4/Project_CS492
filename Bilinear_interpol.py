import numpy as np
import cv2 as cv

 
def GetBilinearPixel(imArr, posX, posY):
	out = []

	modXi = int(posX)
	modYi = int(posY)
	modXf = posX - modXi
	modYf = posY - modYi
	modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1)
	modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1)
 

	for chan in range(imArr.shape[2]):
		bl = imArr[modYi, modXi, chan]
		br = imArr[modYi, modXiPlusOneLim, chan]
		tl = imArr[modYiPlusOneLim, modXi, chan]
		tr = imArr[modYiPlusOneLim, modXiPlusOneLim, chan]
 

		b = modXf * br + (1. - modXf) * bl
		t = modXf * tr + (1. - modXf) * tl
		pxf = modYf * t + (1. - modYf) * b
		out.append(int(pxf))

 
	return out

 
im = cv.imread('new.png')
enlargedShape = list(map(int, [im.shape[0]*2, im.shape[1]*2, im.shape[2]]))
enlargedImg = np.empty(enlargedShape, dtype=np.uint8)
rowScale = float(im.shape[0]) / float(enlargedImg.shape[0])
colScale = float(im.shape[1]) / float(enlargedImg.shape[1])

for r in range(enlargedImg.shape[0]):
	for c in range(enlargedImg.shape[1]):
		orir = r * rowScale
		oric = c * colScale
		enlargedImg[r, c] = GetBilinearPixel(im, oric, orir)
cv.imshow("cropped",im)
cv.waitKey(0)
cv.imshow("cropped",enlargedImg)
cv.waitKey(0)
 
