import cv2
filename = '/home/jps/Pictures/input.jpg'

oriimage = cv2.imread(filename)

print oriimage.shape
newx,newy = oriimage.shape[1]/4,oriimage.shape[0]/4 #new size (w,h)

newimage = cv2.resize(oriimage,(newx,newy))

print newimage.shape

small = cv2.resize(oriimage, (0,0), fx=0.5, fy=0.5)
large = cv2.resize(oriimage, (0,0), fx=1.5, fy=1.5)

crop_img = oriimage[0:400, 0:300] # Crop from {x, y, w, h } => {0, 0, 300, 400}

cv2.imshow("original image",oriimage)
cv2.imshow("resize image",newimage)
cv2.imshow("small image",small)
cv2.imshow("large image",large)
cv2.imshow("cropped", crop_img)


cv2.waitKey(0)