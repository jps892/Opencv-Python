import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/home/jps/Pictures/input.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
plt.imshow(cl1, 'gray')
plt.title('adaptive_histogram')
plt.show()