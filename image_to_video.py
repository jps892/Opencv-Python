import cv2
import numpy as np
import glob
import random

def rotate1(imag1, angle):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    dst = image
    k1 = int(img.shape[0] - dst.shape[0]) / 2
    k2 = int(img.shape[1] - dst.shape[1]) / 2
    img[k1:dst.shape[0] + k1, k2:dst.shape[1] + k2] = dst[0:dst.shape[0], 0:dst.shape[1]]
    M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), angle, 1)
    img1 = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return img1

def zoomin1(imag1, f_x, f_y):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    dst = cv2.resize(imag1, None, fx=f_x, fy=f_y, interpolation=cv2.INTER_LINEAR)
    k1 = int(img.shape[0]-dst.shape[0])/2
    k2 = int(img.shape[1]-dst.shape[1])/2
    img[k1:dst.shape[0]+k1, k2:dst.shape[1]+k2] = dst[0:dst.shape[0], 0:dst.shape[1]]

    return img


def zoomout1(imag1, f_x, f_y):
    img = np.zeros((imag1.shape[0]+100, imag1.shape[1]+100, imag1.shape[2]), dtype=np.uint8)
    dst = cv2.resize(imag1, None, fx=f_x, fy=f_y, interpolation=cv2.INTER_LINEAR)
    k1 = int(img.shape[0] - dst.shape[0]) / 2
    k2 = int(img.shape[1] - dst.shape[1]) / 2
    print img.shape, dst.shape, k1, k2
    img[k1:dst.shape[0] + k1, k2:dst.shape[1] + k2] = dst[0:dst.shape[0], 0:dst.shape[1]]

    return img

def up1(imag1, x):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    k1 = int(img.shape[0] - imag1.shape[0]) / 2
    k2 = int(img.shape[1] - imag1.shape[1]) / 2
    img [k1-x:imag1.shape[0]+k1-x, k2:imag1.shape[1]+k2] = imag1 [0:imag1.shape[0], 0:imag1.shape[1]]
    return img

def down1(imag1, x):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    k1 = int(img.shape[0] - imag1.shape[0]) / 2
    k2 = int(img.shape[1] - imag1.shape[1]) / 2
    img[k1 + x:imag1.shape[0] + k1 + x, k2:imag1.shape[1] + k2] = imag1[0:imag1.shape[0], 0:imag1.shape[1]]
    return img

def left1(imag1, x):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    k1 = int(img.shape[0] - imag1.shape[0]) / 2
    k2 = int(img.shape[1] - imag1.shape[1]) / 2
    img [k1:imag1.shape[0]+k1, k2-x:imag1.shape[1]+k2-x] = imag1 [0:imag1.shape[0], 0:imag1.shape[1]]
    return img

def right1(imag1, x):
    img = np.zeros((imag1.shape[0] + 100, imag1.shape[1] + 100, imag1.shape[2]), dtype=np.uint8)
    k1 = int(img.shape[0] - imag1.shape[0]) / 2
    k2 = int(img.shape[1] - imag1.shape[1]) / 2
    img [k1:imag1.shape[0]+k1, k2+x:imag1.shape[1]+k2+x] = imag1 [0:imag1.shape[0], 0:imag1.shape[1]]
    return img

def zoomout(image, ii):
    imageout = image
    for i in range(1,ii):
        dst = zoomout1(imageout, 1+(0.02*i/4), 1+(0.02*i/4))
        MOV.write(dst)
    for i in range(1, ii):
        dst = zoomout1(imageout, 1 + (0.02 * (ii-i)/4), 1 + (0.02 * (ii-i)/4))
        MOV.write(dst)

def zoomin(image, ii):
    for i in range(1, ii):
        dst = zoomin1(image, 1 - (0.02 * (i)/4), 1 - (0.02 * (i)/4))
        MOV.write(dst)
    for i in range(1, ii):
        dst = zoomin1(image, 1 - (0.02 * (ii-i)/4), 1 - (0.02 * (ii-i)/4))
        MOV.write(dst)

def up(image, ii):
    for i in range(1, ii):
        dst = up1(image, 16 * i/4)
        MOV.write(dst)
    for i in range(1, ii):
        dst = up1(image, 16 * (ii - i)/4)
        MOV.write(dst)

def down(image, ii):
    for i in range(1,ii):
        dst = down1(image, 16*i/4)
        MOV.write(dst)
    for i in range(1, ii):
        dst = down1(image, 16 * (ii-i)/4)
        MOV.write(dst)

def left(image, ii):
    for i in range(1, ii):
        dst = left1(image, 16 * i/4)
        MOV.write(dst)
    for i in range(1, ii):
        dst = left1(image, 16 * (ii - i)/4)
        MOV.write(dst)

def right(image, ii):
    for i in range(1, ii):
        dst = right1(image, 16 * i/4)
        MOV.write(dst)
    for i in range(1, ii):
        dst = right1(image, 16 * (ii - i)/4)
        MOV.write(dst)

def rotate_clockwise(image, ii):
    for i in range(1,ii):
        dst = rotate1(image, 1.2*i/4)
        MOV.write(dst)
    for i in range(1,ii):
        dst = rotate1(image, 1.2*(ii-i)/4)
        MOV.write(dst)

def rotate_anti_clockwise(image, ii):
    for i in range(1,ii):
        dst = rotate1(image, -1.2*i/4)
        MOV.write(dst)
    for i in range(1,ii):
        dst = rotate1(image, -1.2*(ii-i)/4)
        MOV.write(dst)


nIMAGES = 1
files = glob.glob('/home/jps/Downloads/VIDEO_corpus/sheet_pipe_videos/images/sheet_pile_22.jpg.jpg' )
ik = cv2.imread('/home/jps/Downloads/VIDEO_corpus/sheet_pipe_videos/images/sheet_pile_22.jpg.jpg')
sk = ik.shape
print sk[1]
mov = '/home/jps/Downloads/VIDEO_corpus/'+ 'sheet_pile.avi'
MOV = cv2.VideoWriter(filename=mov, fourcc=cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), fps=25, frameSize=(sk[1]+100, sk[0]+100))
for i in np.arange(0, nIMAGES):
    print 'Working on: ' +files[0][-14:-4]
    image = cv2.imread(files[0], -1)
    m = np.zeros((sk[0]+10, sk[0]+10, 3), dtype=np.uint8)
    imageout = image;

    zoomout(image, 7)

    zoomin(image, 7)

    up(image, 7)

    down(image, 7)

    left(image, 7)

    right(image, 7)

    rotate_clockwise(image, 8)

    rotate_anti_clockwise(image, 8)


    # dst = rotate(image, sk[1], sk[0], 20)
    # dst = shear()

    # pts1 = np.float32([[0, 0], [sk[1], sk[0]], [0, sk[0]-200]])
    # pts2 = np.float32([[0, 200], [sk[1], sk[0]], [0, sk[0]]])
    #
    # M = cv2.getAffineTransform(pts1, pts2)
    # dst = cv2.warpAffine(image, M, (sk[1], sk[0]))


    # MOV.write(dst)

     #/home/jps/Desktop/videocorp/CORP/circular_pipes_1.jpg.jpgcrop y:h, x:w

 # now let's create the movie:
 #    crop_image = cv2.applyColorMap(crop_image, 1)
 #    cv2.imshow("image", dst)
 #    cv2.waitKey(0)
 #    cv2.destroyAllWindows()


MOV.release()