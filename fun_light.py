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
    contrast = level / 100
    brightness = 0
    nimg = contrast_brightness(img, brightness, contrast)
    return nimg

def brightness(img, level):
    contrast = 0
    brightness = level / 100
    nimg = contrast_brightness(img, brightness, contrast)
    return nimg

def contrast_brightness(img, brightness, contrast):
    b = brightness
    c = contrast
    k = math.tan( (45 + 44 * c) / 180 * math.pi );  
#    b, c value range are [-1,1]
    
    nimg = img
    
    p = np.zeros(256)
    for i in range(256):
        p[i] = (i - 127.5 * (1 - b)) * k + 127.5 * (1 + b)
    p = np.clip(p, 0, 255)
    fimg = img.flatten()
    for i in range(len(fimg)):
        fimg[i] = p[fimg[i]]
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
