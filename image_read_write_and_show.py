import cv2

PATH_NAME = '/home/jps/Pictures/resized_H/h_pipes_118.jpg.jpg'


if __name__ == '__main__':
    #read
    img = cv2.imread(PATH_NAME)

    #write
    cv2.imwrite('/home/jps/H_pile.png', img)

    #show
    cv2.imshow("Contour", img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()