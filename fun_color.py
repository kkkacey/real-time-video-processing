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

def HSL(img, shift, option):
    if option == "hue":
        new_img = hue(img, shift)
    elif option == "saturation":
        new_img = saturation(img, shift)
    elif option == "luminance":
        new_img = luminance(img, shift)
    else:
#        print('error in HSL')
        new_img = img
    return new_img

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
def color_HSL(img, color, shift, option):
    if option == 'hue':
        new_img = color_hue(img, color, shift)
    elif option == 'saturation':
        new_img = color_saturation(img, color, shift)
    else:
#        print('error in color_HSL')
        new_img = img
    return new_img

    
def color_hue (img, color, shift):
#    nimg = img
    hsv_color = color_hsv(color)
    hue = hsv_color[0,0,0]
#        cv2.imshow('red', img)
#    segment = img[:,:,channel]   
        
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([hue-20, 40, 40])
    upper = np.array([hue+20, 255, 255])
    color_mask = cv2.inRange(img_hsv, lower, upper)
    
#    img_hsv_shift = cv2.add(img_hsv, np.array([shift, 0, 0]), mask = color_mask)
    img_hsv_shift = img_hsv
#    for chan in range(3):
#        img_hsv_shift[:,:,chan] = np.dot((img_hsv + [shift, 0, 0])[:,:,chan], color_mask)
    img_hsv_mask_shift = cv2.add(img_hsv[:,:,0], shift, mask = color_mask)
    img_hsv_shift[:,:,0] = cv2.add(img_hsv_mask_shift, img_hsv[:,:,0], mask = 1 - color_mask)
    img_hsv_shift = np.uint8(img_hsv_shift)
    
#    segment = cv2.bitwise_and(img_hsv, img_hsv_shift, mask = color_mask)
    
    reverse_bgr_img = cv2.cvtColor(img_hsv_shift, cv2.COLOR_HSV2BGR)
#    for chan in range(3):
#        nimg[:,:,chan] = reverse_bgr_img[:,:,chan]
    return reverse_bgr_img
    
def color_saturation (img, color, shift):
    nimg = img    
    
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


def color_hsv(color):
    if color == 'red':
        color_rgb = np.uint8([[[0, 0, 255]]])
    elif color == 'green':
        color_rgb = np.uint8([[[0, 255, 0]]])
    elif color == 'blue':
        color_rgb = np.uint8([[[255, 0, 0]]])
    elif color == 'yellow':
        color_rgb = np.uint8([[[0, 255, 255]]])
    elif color == 'magenta':
        color_rgb = np.uint8([[[255, 0, 255]]])
    elif color == 'cyan':
        color_rgb = np.uint8([[[255, 255, 0]]])
    else:
        print('input color error!')
    color_hsv = cv2.cvtColor(color_rgb, cv2.COLOR_BGR2HSV)
    return color_hsv