import cv2
import numpy as np

img = cv2.imread('/home/jps/Pictures/input.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((100,100),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()