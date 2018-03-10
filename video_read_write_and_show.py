import cv2
import numpy as np


nIMAGES = 150;
PATH_NAME = '/home/jps/Downloads/image_corpus (2)/CMVP-253/circle_corp_videos/VID_20170923_113247759.mp4'
mov = '/home/jps/Downloads/image_corpus (2)/CMVP-253/circle_corp_videos/'+ 'rectangle_video_corpus_3i.avi'
MOV = cv2.VideoWriter(filename=mov, fourcc=cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), fps=25, frameSize=(1920, 1080))

cap = cv2.VideoCapture(PATH_NAME)

if __name__ == '__main__':
    for i in np.arange(0, nIMAGES):

        # Capture frame-by-frame
        ret, frame = cap.read()

        #shape
        print frame.shape

        #BGR2GRAY
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #write video
        MOV.write(frame)

        #Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
