import cv2
import numpy

image1= cv2.imread("cr7.jpg")

image1.shape

image2= cv2.imread("lm10.jpg")

image2.shape

image2= image2[:764,:]

image2.shape

collage= numpy.concatenate((image1,image2),axis=1)

cv2.imshow("Collage",collage)

cv2.waitKey()

cv2.destroyAllWindows()

