import cv2

PATH_NAME = '/home/jps/Pictures/resized_H/h_pipes_118.jpg.jpg'


if __name__ == '__main__':
    img = cv2.imread(PATH_NAME)

    cv2.imwrite('/home/jps/H_pile.png', img)
    cv2.imshow("Contour", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()