# -*- coding: utf-8 -*-
"""
functions of the light
"""

import numpy as np
import math
import cv2

def light(img, level, option):
    if option == 'contrast':
        new_img = contrast(img, level)
#        new_img = auto_contrast(img, level)
    elif option == 'brightness':
        new_img = brightness(img, level)
    elif option == 'highlight':
        new_img = highlight(img, level)
    elif option == 'white levels':
        new_img = whitehist(img, level)
    elif option == 'shadows':
        new_img = shadows(img, level)
    elif option == 'black levels':
        new_img = blackhist(img, level)
    else:
#        print('error in light')
        new_img = img
    return new_img
    
def contrast(img, level):
    if level == 10:
        nimg = auto_contrast(img, level)
    else:
        contrast = level / 100
        brightness = 0
        nimg = contrast_brightness(img, brightness, contrast)
    return nimg

def brightness(img, level):
#    contrast = 0
#    brightness = level / 100
#    nimg = contrast_brightness(img, brightness, contrast)
    
#    gamma correction: enhance exposure and decrease the contrast
    nimg = img
    gamma = 1 - level / 20
    p = np.zeros(256)
    for i in range(256):
        p[i] = (i /255) ** gamma * 255
    p = np.clip(p, 0, 255)
    for i in range(3):
        nimg[:,:,i] = p[img[:,:,i]]
        
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
    for i in range(3):
     nimg[:,:,i] = p[img[:,:,i]]
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


#    hightlight: the most bright part of the image
def highlight(img, level):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hightligt_max = img_hsv[:,:,2].max()
    
    kernel = np.ones((3,3))
    kernel = kernel / sum(kernel)
    lower = np.array([0, 0, hightligt_max - np.abs(level) * 5])
    upper = np.array([255, 255, hightligt_max])
    highlight_mask = cv2.inRange(img_hsv, lower, upper)   
    highlight_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = highlight_mask)
    highlight_removed = np.uint8(np.clip(highlight_segment - [0, 0, level*2], 0, 255))
    untouch_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = 255 - highlight_mask)
    nimg_hsv = cv2.bitwise_or(highlight_removed, untouch_segment)
    reverse_bgr_img = cv2.cvtColor(nimg_hsv, cv2.COLOR_HSV2BGR)
    return reverse_bgr_img

def shadows(img, level):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    shadows_min = img_hsv[:,:,2].min()
    
    kernel = np.ones((3,3))
    kernel = kernel / sum(kernel)
    lower = np.array([0, 0, shadows_min])
    upper = np.array([255, 255, shadows_min + np.abs(level) * 3])
    mask = cv2.inRange(img_hsv, lower, upper)   
    highlight_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)
    shadows_removed = np.uint8(np.clip(highlight_segment + [0, 0, level], 0, 255))
    untouch_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = 255 - mask)
    nimg_hsv = cv2.bitwise_or(shadows_removed, untouch_segment)
    reverse_bgr_img = cv2.cvtColor(nimg_hsv, cv2.COLOR_HSV2BGR)
    return reverse_bgr_img

#    white: the relatively bright part of the image
def whitehist(img, level):
    nimg = img
    if level != 0:
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        a = np.abs(level) / 50
        f = np.cumsum(np.ones((256,1)))
        cutoff = np.abs(level) * 8
        if level > 0:
            g_high = f[0:cutoff] ** 3 * a
        elif level < 0:
            g_high = np.log(f[0:cutoff]) * a
        g_high = g_high * cutoff / g_high.max() - cutoff + 256
        g = np.append(f[0:256 - cutoff], g_high)
        g = np.clip(g, 0, 255)
        img_hsv[:,:,2] = g[img_hsv[:,:,2]] 
        
        nimg = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    return nimg

def blackhist(img, level):
    nimg = img
    if level != 0:
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        a = np.abs(level) / 80
        f = np.cumsum(np.ones((256,1)))
        cutoff = np.abs(level) * 8
        if level > 0:
            g_low = np.log(f[0:cutoff] ) * a
        elif level < 0:
            g_low = f[0:cutoff] ** 3 * a
        g_low = g_low * cutoff / g_low.max()
        g_high = f[cutoff:]
        g = np.append(g_low, g_high)
        g = np.clip(g, 0, 255)
        
        img_hsv[:,:,2] = g[img_hsv[:,:,2]] 
        
        nimg = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    return nimg