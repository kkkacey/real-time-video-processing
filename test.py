# -*- coding: utf-8 -*-
"""
testing functions
"""

import cv2
import fun_color

img = cv2.imread('save.jpg')

color = 'red'

nimg = fun_color.color_hue(img, color, 20)

cv2.imshow('new img', nimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
