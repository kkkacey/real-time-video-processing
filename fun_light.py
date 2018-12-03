# -*- coding: utf-8 -*-
"""
functions of the light
"""

import numpy as np
import math


# contrast & contrast
def contrast_brightness(img, level):
    B = brightness / 255.
    c = contrast / 255.
    k = math.tan( (45 + 44 * c) / 180 * math.pi );
    
    nimg = img
    
    fimg = img.flatten()
    for i in range(len(fimg)):
        nimg[i] = (i - 127.5 * (1 - B)) * k + 127.5 * (1 + B)
    
    nimg = np.reshape(nimg, np.shape(img))
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
