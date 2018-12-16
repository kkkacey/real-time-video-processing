# -*- coding: utf-8 -*-
"""
color space alternations
H, S, V ...  in a seperate color
"""

import cv2
import numpy as np


def HSL(img, shift, option):
    if option == "hue":
        new_img = hue(img, shift)
    elif option == "saturation":
        new_img = saturation(img, shift)
#        new_img = naturalsaturation(img, shift)
    elif option == "luminance":
        new_img = luminance(img, shift)
    else:
#        print('error in HSL')
        new_img = img
    return new_img

# overall hue
def hue (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.uint8(np.clip(img_hsv + [shift, 0, 0], 0, 255))
    reverse_bgr_img = np.clip(cv2.cvtColor(hue, cv2.COLOR_HSV2BGR), 0, 255)
    return reverse_bgr_img

# overall sturation
def saturation (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.uint8(np.clip(img_hsv + [0, shift, 0], 0, 255))
    reverse_bgr_img = np.clip(cv2.cvtColor(hue, cv2.COLOR_HSV2BGR), 0, 255)
    return reverse_bgr_img

#def naturalsaturation(img, shift):
#    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#    nimg_hsv = img_hsv
#    if shift != 0:
#        p = np.zeros(256)
#        if shift > 0:
#            r = - shift / 200
#            a =  * shift
#            for i in range(1, 256):
#                p[i] = -i ** r * a + 1
#        elif shift < 0:
#            r = - shift / 2
#            for i in range(1, 256):
#                p[i] = i ** r + 1
#    #    p = np.clip(p, 0, 255)
#        p = p * 256 / p.max()
#        nimg_hsv[:,:,1] = p[img_hsv[:,:,1]]
#    nimg = np.clip(cv2.cvtColor(nimg_hsv, cv2.COLOR_HSV2BGR), 0, 255)
#    return nimg, p
    
# overall luminance
def luminance (img, shift):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = np.uint8(np.clip(img_hsv + [0, 0, shift], 0, 255))
    reverse_bgr_img = np.clip(cv2.cvtColor(hue, cv2.COLOR_HSV2BGR), 0, 255)
    return reverse_bgr_img



# color-wise HSL
def color_HSL(img, color, shift, option):
    if option == 'hue':
        new_img = color_hue(img, color, shift)
    elif option == 'saturation':
        new_img = color_saturation(img, color, shift)
    elif option == 'luminance':
        new_img = color_luminance(img, color, shift)
    else:
        print('error in color_HSL')
        new_img = img
    return new_img

    
def color_hue (img, color, shift):
    hsv_color = color_hsv(color)
    hue = hsv_color[0,0,0]
        
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([hue-20, 40, 40])
    upper = np.array([hue+20, 255, 255])
    color_mask = cv2.inRange(img_hsv, lower, upper)
    
#    img_hsv_shift = cv2.add(img_hsv, np.array([shift, 0, 0]), mask = color_mask)
#    img_hsv_shift = img_hsv
#    img_hsv_mask_shift = cv2.add(img_hsv[:,:,0], shift, mask = color_mask)
#    img_hsv_shift[:,:,0] = cv2.add(img_hsv_mask_shift, img_hsv[:,:,0], mask = 1 - color_mask)
#    img_hsv_shift = np.uint8(img_hsv_shift)
    
    img_hue_shift = np.uint8(np.clip(img_hsv + [shift, 0, 0], 0, 255))
    hue_shift_segment = cv2.bitwise_and(img_hue_shift, img_hue_shift, mask = color_mask)
    untouch_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = 255 - color_mask)
    img_hsv_final = cv2.bitwise_or(hue_shift_segment, untouch_segment)
    
    
    reverse_bgr_img = np.clip(cv2.cvtColor(img_hsv_final, cv2.COLOR_HSV2BGR), 0, 255)
    return reverse_bgr_img
    
def color_saturation (img, color, shift):
    hsv_color = color_hsv(color)
    hue = hsv_color[0,0,0]
        
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([hue-20, 40, 40])
    upper = np.array([hue+20, 255, 255])
    color_mask = cv2.inRange(img_hsv, lower, upper)
    
    img_shift = np.uint8(np.clip(img_hsv + [0, shift, 0], 0, 255))
    shift_segment = cv2.bitwise_and(img_shift, img_shift, mask = color_mask)
    untouch_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = 255 - color_mask)
    img_hsv_final = cv2.bitwise_or(shift_segment, untouch_segment)
    
    nimg = np.clip(cv2.cvtColor(img_hsv_final, cv2.COLOR_HSV2BGR), 0, 255)
    return nimg

def color_luminance(img, color, shift):
    hsv_color = color_hsv(color)
    hue = hsv_color[0,0,0]
        
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([hue-20, 40, 40])
    upper = np.array([hue+20, 255, 255])
    color_mask = cv2.inRange(img_hsv, lower, upper)
    
    img_shift = np.uint8(np.clip(img_hsv + [0, 0, shift], 0, 255))
    shift_segment = cv2.bitwise_and(img_shift, img_shift, mask = color_mask)
    untouch_segment = cv2.bitwise_and(img_hsv, img_hsv, mask = 255 - color_mask)
    img_hsv_final = cv2.bitwise_or(shift_segment, untouch_segment)
    
    nimg = np.clip(cv2.cvtColor(img_hsv_final, cv2.COLOR_HSV2BGR), 0, 255)
    return nimg


def color_hsv(color):
    if color == 'red':
        color_rgb = np.uint8([[[0, 0, 255]]])
    elif color == 'green':
        color_rgb = np.uint8([[[0, 255, 0]]])
    elif color == 'blue':
        color_rgb = np.uint8([[[255, 0, 0]]])
    elif color == 'yellow':
        color_rgb = np.uint8([[[0, 255, 255]]])
    elif color == 'orange':
        color_rgb = np.uint8([[[0, 128, 255]]])
    elif color == 'cyan':
        color_rgb = np.uint8([[[255, 255, 0]]])
    else:
        print('input color error!')
    color_hsv = cv2.cvtColor(color_rgb, cv2.COLOR_BGR2HSV)
    return color_hsv