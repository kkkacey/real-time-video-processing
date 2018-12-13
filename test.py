# -*- coding: utf-8 -*-
"""
testing functions
"""

import cv2
import fun_color
import fun_detail
import numpy as np

def clip_img(img):
    (rows, cols, chan) = img.shape
    for i in range(rows):
        for j in range(cols):
            for n in range(chan):
                if img[i,j,n] > 255:
                    img[i,j,n] = 255
                elif img[i,j,n] < 0:
                    img[i,j,n] = 0
    return img

img = cv2.imread('save.jpg')

color = 'blue'

nimg = fun_color.HSL(img, 10, 'hue')

nimg = nimg.astype(np.uint8)

cv2.imshow('original', img)
cv2.imshow('new img', nimg)
#print(clip_img(nimg))

cv2.waitKey(0)
cv2.destroyAllWindows()


