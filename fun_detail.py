# -*- coding: utf-8 -*-
"""
filtering functions
"""

import cv2
import numpy as np

def detail(img, shift, option):
    if option == "blur":
        new_img = blur(img, shift)
    elif option == "sharpen":
        new_img = sharpen(img, shift)
    else:
#        print('error in detail')
        new_img = img
    return new_img

def blur (img, shift):
    blur_kernel_size = (shift * 2 + 1, shift * 2 + 1)
    new_img = cv2.GaussianBlur(img, blur_kernel_size, sigmaX = 2, sigmaY = 2)
#    deblur: deconvolution (P498 of CV book)
#    should write an implementation, since no built in function
#    https://github.com/opencv/opencv/blob/master/samples/python/deconvolution.py
#    http://scikit-image.org/docs/dev/auto_examples/filters/plot_deconvolution.html
    return new_img

def sharpen(img, shift):
#    kernel = np.array(np.dot([[0,-1,0], [-1,15 - shift,-1], [0,-1,0]], 1/(11-shift)))
#    kernel = np.array(np.dot([[-1,-1,-1], [-1,19 - shift,-1], [-1,-1,-1]], 1/(11-shift)))
    blur_kernel = np.ones((3,3))
    blur_kernel = blur_kernel / np.sum(blur_kernel)
    lam = np.abs(shift)/50
    new_img = img + np.dot(lam, ( img - cv2.filter2D(img, -1, blur_kernel) ) )
#            this sharpen algorithm is like adding noise to the blurred image
#            not as expected as sharpening edges and add noise when the level is high
#            find a better sharpen algorithm instead, write this comparison into the report
#            build GUI as soon as possible
#    the illustrated unsharpen method is not desired.
    return new_img


# denoise: use average filter insatead of gaussian filter?
    
# add noise points

# edge detection