# -*- coding: utf-8 -*-
"""
color space alternations
H, S, V ...  in a seperate color
"""

import cv2
import numpy as np

# temperature
# tint
# vibrance (自然饱和度)
# saturation （饱和度）


# overall hue
def hue (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    TODO: hue range should not exceeds [0,180]
    hue = np.uint8(img_hsv + [shift, 0, 0])
    reverse_bgr_img = cv2.cvtColor(hue, cv2.COLOR_HSV2BGR)
    return reverse_bgr_img

# overall sturation
def saturation (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    TODO: range should not exceeds [0,255]
    hue = np.uint8(img_hsv + [0, shift, 0])
    reverse_bgr_img = cv2.cvtColor(hue, cv2.COLOR_HSV2BGR)
    return reverse_bgr_img
    
# overall luminance
def luminance (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    TODO: range should not exceeds [0,255]
    hue = np.uint8(img_hsv + [0, 0, shift])
    reverse_bgr_img = cv2.cvtColor(hue, cv2.COLOR_HSV2BGR)
    return reverse_bgr_img




# color-wise HSL
    
def color_hue (img, color, shift):
    nimg = img    
    if color == 'red':
        channel = [2]
    elif color == 'green':
        channel = [1]
    elif color == 'blue':
        channel = [0]
    elif color == 'yellow':
        channel = [1, 2]
    elif color == 'magenta':
        channel = [0, 2]
    elif color == 'cyan':
        channel = [0, 1]
    else:
        print('input color error!')
#        cv2.imshow('red', img)
#    segment = img[:,:,channel]
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.uint8(img_hsv + [shift, 0, 0])
    reverse_bgr_img = cv2.cvtColor(hue, cv2.COLOR_HSV2BGR)
    for chan in channel:
        nimg[:,:,chan] = reverse_bgr_img[:,:,chan]
    return nimg
    
def color_saturation (img, color, shift):
    nimg = img    
    if color == 'red':
        channel = [2]
    elif color == 'green':
        channel = [1]
    elif color == 'blue':
        channel = [0]
    elif color == 'yellow':
        channel = [1, 2]
    elif color == 'magenta':
        channel = [0, 2]
    elif color == 'cyan':
        channel = [0, 1]
    else:
        print('input color error!')
#        cv2.imshow('red', img)
#    segment = img[:,:,channel]
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.uint8(img_hsv + [0, shift, 0])
    reverse_bgr_img = cv2.cvtColor(hue, cv2.COLOR_HSV2BGR)
    for chan in channel:
        nimg[:,:,chan] = reverse_bgr_img[:,:,chan]
    return nimg
    # hue
    # saturation
    # light
