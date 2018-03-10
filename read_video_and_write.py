import numpy as np
import cv2

nIMAGES = 25*30
mov = '/home/jps/Desktop/circle_video_corpus_3i_2.avi'
MOV = cv2.VideoWriter(filename=mov, fourcc=cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), fps=25, frameSize=(640, 480))

cap = cv2.VideoCapture(1)

for i in np.arange(0, nIMAGES):
    # Capture frame-by-frame
    ret, frame = cap.read()
    MOV.write(frame)

    # # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
MOV.release()
cap.release()
cv2.destroyAllWindows()