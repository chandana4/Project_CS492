import cv2
import numpy as np

# load the image
image = cv2.imread('pic.jpg')
height=image.shape[0]
width=image.shape[1]
print height,width
M = height//2
N = width//3
count=0
for y in range(0,height,M):
    for x in range(0,width, N):
        y1 = y + M
        x1 = x + N
	if y1>height or x1>width:
		break;
	crop_img = image[y:y+M,x:x+N]
	cv2.imshow("cropped"+str(count), crop_img)
	count+=1
	cv2.waitKey(0)
# show image and patch
cv2.destroyAllWindows()

