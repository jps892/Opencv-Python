import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yuv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    ycrcb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    cv2.imshow("Gray", gray_frame)
    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("YUV", yuv_frame)
    cv2.imshow("YCrCb", ycrcb_frame)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

