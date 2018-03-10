import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
circles_count = 0

while True:
    ret, frame = video_capture.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_frame = cv2.GaussianBlur(gray_frame, (19,19), sigmaX=3, sigmaY=3)

    circles = cv2.HoughCircles(gray_frame, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=50, param2=50, minRadius=50, maxRadius=160)

    if(circles != None):
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 2)
            # draw the center of the circle
            # cv2.circle(frame, (i[0], i[1]), 2, (255, 0, 0), 2)

            circles_count += 1
            cv2.putText(frame, str(circles_count), (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0))

    cv2.imshow("Source", frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

