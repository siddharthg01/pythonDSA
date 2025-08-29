import cv2 as c

import numpy as n

img = c.imread("C:/New python/OpenCV/gitimg.jpg")

width= 600
height= 650

dim=(width, height)

resized= c.resize(img, dim)
kernel= n.ones((5,5), dtype='uint8')

""" erosion= c.erode(resized, kernel, iterations=1)
dilation = c.dilate(resized, kernel, iterations=1) """
""" opening= c.morphologyEx(resized, c.MORPH_OPEN,kernel)
closing= c.morphologyEx(resized, c.MORPH_CLOSE,kernel) """

gradient= c.morphologyEx(resized, c.MORPH_GRADIENT , kernel)
tophat= c.morphologyEx(resized, c.MORPH_TOPHAT, kernel)
blackhat= c.morphologyEx(resized, c.MORPH_BLACKHAT, kernel)


c.imshow("Original", resized)
c.imshow("Gradient",gradient)
c.imshow("TOP HAT",tophat)
c.imshow("Black hat", blackhat)


""" c.imshow("Erosion", erosion)
c.imshow("Dilation", dilation) """

c.waitKey(0)
c.destroyAllWindows()

