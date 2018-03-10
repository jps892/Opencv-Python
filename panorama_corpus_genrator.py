import cv2
import numpy as np
import glob
import random

nIMAGES = 351*3
files = glob.glob('/home/jps/Downloads/merge_from_ofoct (2).jpg' )
ik = cv2.imread('/home/jps/Downloads/merge_from_ofoct (2).jpg')
sk = ik.shape
print sk
mov = '/home/jps/Downloads/'+ 'circle_2.avi'
MOV = cv2.VideoWriter(filename=mov, fourcc=cv2.VideoWriter_fourcc('F', 'M', 'P', '4'), fps=25, frameSize=(640, sk[0]))
for i in np.arange(1, nIMAGES):
    print 'Working on: ' +files[0][-14:-4]
    image = cv2.imread(files[0], -1)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    print (0+4*i), (640+4*i)
    imageout = image[0:sk[0], (0+4*i):(640+4*i)];

    # cv2.imshow("imageout", imageout)
    # cv2.waitKey(0)

    MOV.write(imageout)
    # MOV.write(dst)

     #/home/jps/Desktop/videocorp/CORP/circular_pipes_1.jpg.jpgcrop y:h, x:w

 # now let's create the movie:
 #    crop_image = cv2.applyColorMap(crop_image, 1)
 #    cv2.imshow("image", dst)
 #    cv2.waitKey(0)
 #    cv2.destroyAllWindows()


MOV.release()