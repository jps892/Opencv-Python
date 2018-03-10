import cv2
import numpy as np

img = cv2.imread('/home/jps/Pictures/input.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

dilation = cv2.dilate(img,kernel,iterations = 1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite('/home/jps/Pictures/erosion.jpg',erosion)
cv2.imwrite('/home/jps/Pictures/dilation.jpg',dilation)
cv2.imwrite('/home/jps/Pictures/opening.jpg',opening)
cv2.imwrite('/home/jps/Pictures/closing.jpg',closing)
cv2.imwrite('/home/jps/Pictures/gradient.jpg',gradient)
cv2.imwrite('/home/jps/Pictures/tophat.jpg',tophat)
cv2.imwrite('/home/jps/Pictures/blackhat.jpg',blackhat)