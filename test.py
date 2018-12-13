# -*- coding: utf-8 -*-
"""
testing functions
"""

import cv2
import fun_color
import fun_detail
import tools
import numpy as np


img = cv2.imread('save.jpg')

color = 'blue'
 
#nimg = fun_color.HSL(img, 10, 'hue')

#nimg = fun_detail.sharpen(img, 5)

#nimg = nimg.astype(np.uint8)

nimg = fun_color.color_HSL(img, 'blue', 0, 'hue')

# the functions has done clipping already, but in the wrong way
#nimg = tools.clip_bitwise(nimg, 0, 255)

cv2.imshow('original', img)
cv2.imshow('new img', nimg)
#print(clip_img(nimg))

cv2.waitKey(0)
cv2.destroyAllWindows()


