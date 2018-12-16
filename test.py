# -*- coding: utf-8 -*-
"""
testing functions
"""

import cv2
import fun_color
import fun_detail
import fun_light
import tools
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('save.jpg')

#nimg = nimg.astype(np.uint8

for l in range(1,10):
    nimg,g = fun_color.naturalsaturation(img, l)
    plt.figure()
    plt.plot(g)


#cv2.imshow('original', img)
cv2.imshow('new img', nimg)
#


plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()