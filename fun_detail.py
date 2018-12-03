# -*- coding: utf-8 -*-
"""
filtering functions
"""

import cv2
import numpy as np

def sharpen_and_blur (img, shift):
    if shift == 0: 
        new_img = img
    else:
        kernel = (shift * 2 + 1, shift * 2 + 1)
        new_img = cv2.GaussianBlur(img, kernel, sigmaX = 2, sigmaY = 2)
        if shift < 0: 
#            kernel = np.array(np.dot([[0,-1,0], [-1,15 - shift,-1], [0,-1,0]], 1/(11-shift)))
            kernel = np.array(np.dot([[-1,-1,-1], [-1,19 - shift,-1], [-1,-1,-1]], 1/(11-shift)))
            new_img = cv2.filter2D(img, -1, kernel)
    return new_img


# denoise: use average filter insatead of gaussian filter?
    
# add noise points

# edge detection