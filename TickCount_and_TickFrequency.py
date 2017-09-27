import numpy as np
import cv2


if __name__ == '__main__':

    #image read
    img1 = cv2.imread('lena_std.tif',01)

    #TickCount
    e1 = cv2.getTickCount()

    #for loop
    for i in xrange(5,49,2):
        img1 = cv2.medianBlur(img1,i)

    #Tickcount
    e2 = cv2.getTickCount()

    #calculate time & TickFrequency
    time = (e2 - e1)/cv2.getTickFrequency()

    #show time
    print time

    #show image
    cv2.imshow('lena_std', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
