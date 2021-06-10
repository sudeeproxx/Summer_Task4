import cv2
import numpy

image_1=cv2.imread("image1.jpg")

image_1.shape

crop1= image_1[48:129,102:183]

image_2=cv2.imread("image2.jpg")

image_2.shape

crop2= image_2[51:132,97:178]

swap1=image_1

swap2=image_2

#Now swap the cropped parts
#swap1[48:129,102:183]= crop2

#cv2.imshow("AfterSwap1",swap1)
#cv2.waitKey()
#cv2.destroyAllWindows()

swap2[51:132,97:178]= crop1

cv2.imshow("AfterSwap2",swap2)
cv2.waitKey()
cv2.destroyAllWindows()
