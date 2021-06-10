import cv2

import numpy

photo= numpy.zeros((360,720,3))

photo[:,:]=[255,255,255]

#cv2.imshow("photo",photo)
#cv2.waitKey()
#destroyAllWindows()

photo[0:121,30:690]= [255,0,0]

photo[121:241,30:690] = [0,255,0]

photo[241:,30:690]= [0,0,255]

cv2.imshow("photo",photo)
cv2.waitKey()
destroyAllWindows()
