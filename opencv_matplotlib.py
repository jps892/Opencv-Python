import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/home/jps/Pictures/lena_std.tif')
img2 = cv2.imread('/home/jps/Pictures/opencv_logo.jpg')
imgg1 = cv2.imread('/home/jps/Pictures/lena_std.tif', 0)
imgg2 = cv2.imread('/home/jps/Pictures/opencv_logo.jpg', 0)


plt.subplot(221),plt.imshow(img1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(imgg1),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img2),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(imgg2),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()