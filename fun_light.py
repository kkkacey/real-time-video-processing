# -*- coding: utf-8 -*-
"""
functions of the light
"""

import numpy as np
import math

def light(img, level, option):
    if option == 'contrast':
        new_img = contrast(img, level)
    elif option == 'brightness':
        new_img = brightness(img, level)
    else:
#        print('error in light')
        new_img = img
    return new_img
    
def contrast(img, level):
    contrast = level
    brightness = 255
    nimg = contrast_brightness(img, level, brightness, contrast)
    return nimg

def brightness(img, level):
    contrast = 255
    brightness = level
    nimg = contrast_brightness(img, level, brightness, contrast)
    return nimg

def contrast_brightness(img, shift, brightness, contrast):
    B = brightness / 255.
    c = contrast / 255.
    k = math.tan( (45 + 44 * c) / 180 * math.pi );
    
    nimg = img
    
    fimg = img.flatten()
    for i in range(len(fimg)):
        fimg[i] = (i - 127.5 * (1 - B)) * k + 127.5 * (1 + B)
    
    nimg = np.reshape(fimg, img.shape)
    return nimg

# automated-contrast augmentation
def auto_contrast(img, level):
    img_histeq = img
    if level != 0:
        for i in range(3):
            hist,bins = np.histogram(img[:,:,i].flatten(), 256, [0,256])
            cdf = hist.cumsum()
            cdf_normalized = cdf * 255 / cdf.max()
            img_histeq[:,:,i] = cdf_normalized[img[:,:,i]]  
    return img_histeq

# exposure

# brightness


# optional below

# highlights
# shadows
