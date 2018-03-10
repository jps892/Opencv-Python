import cv2
import numpy as np


nIMAGES = 150;
PATH_NAME = '/home/jps/Downloads/VIDEO_corpus/sheet_pile_36.avi'

cap = cv2.VideoCapture(PATH_NAME)

if __name__ == '__main__':
    for i in np.arange(0, nIMAGES):

        # Capture frame-by-frame
        ret, frame = cap.read()

        #frame no
        print i

        #Display the resulting frame
        cv2.imshow('frame',frame)
        cv2.waitKey(100)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()