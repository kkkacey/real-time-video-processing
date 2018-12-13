# -*- coding: utf-8 -*-
"""
"""

import sys
import numpy as np 
import cv2
import tkinter as Tk 
#import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk

import fun_detail
import fun_GUI
import fun_color
import fun_light
#import tools

global new_shift
global new_box

def apply(img, box, shift):
    end_img = img
    if box[0].get() != '':
        option = box[0].get()
        end_img = fun_detail.detail(end_img, shift[0].get(), option)    
        end_img = end_img.astype(np.uint8)
    if box[1].get() != '':
        option = box[1].get()
        end_img = fun_light.light(end_img, shift[1].get(), option)
        end_img = end_img.astype(np.uint8)
    if box[2].get() != '':
        if (shift[2].get() == 0) & (box[3].get() != '') & (shift[3].get() != 0):
            color = box[3].get()
            option = box[2].get()
            end_img = fun_color.color_HSL(end_img, color, shift[3].get(), option)
            end_img = end_img.astype(np.uint8)
        elif shift[2].get() != 0:
            option = box[2].get()
            end_img = fun_color.HSL(end_img, shift[2].get(), option)
            end_img = end_img.astype(np.uint8)
            if (box[3].get() != '') & (shift[3].get() != 0):
                color = box[3].get()
                option = box[2].get()
                end_img = fun_color.color_HSL(end_img, color, shift[3].get(), option)
                end_img = end_img.astype(np.uint8)
        else:
            print('error!')
    return end_img

saved_options = []
    
def apply_get(shift, box):
    global saved_options
    for i in range(len(box) - 1):
        if (box[i].get() != '') & (shift[i].get() != 0):
            saved_options.append([i, box[i].get(), shift[i].get()])
            shift[i].set(0)
        elif (i == 2) & (box[3].get() != '') & (shift[3].get() != 0):
            saved_options.append([3, box[2].get(), shift[3].get(), box[3].get()])
            shift[3].set(0)
    print('options saved!')
    print(saved_options)
    
def apply_presaved(frame):
    new_frame = frame
    global saved_options
    for i in range(len(saved_options)):
        fun = saved_options[i][0]
        option = saved_options[i][1]
        shift = saved_options[i][2]
        if fun == 0:
            new_frame = fun_detail.detail(new_frame, shift, option)
            new_frame = new_frame.astype(np.uint8)
        elif fun == 1:
            new_frame = fun_light.light(new_frame, shift, option)
            new_frame = new_frame.astype(np.uint8)
        elif fun == 2:
            new_frame = fun_color.HSL(new_frame, shift, option)
            new_frame = new_frame.astype(np.uint8)
        elif fun == 3:
            color = saved_options[i][3]
            new_frame = fun_color.color_HSL(new_frame, color, shift, option)
            new_frame = new_frame.astype(np.uint8)
        else:
            print('erorr in APPLY!')
            print(saved_options)    
    return new_frame

def reset(shift):
    for i in range(len(shift)):
        shift[i].set(0)
    global saved_options
    saved_options = []

top, Canvas, box, shift, B_apply, B_reset = fun_GUI.initGUI()
B_apply.configure(command = lambda: apply_get(shift, box))
B_reset.configure(command = lambda: reset(shift))

cap = cv2.VideoCapture(0)

while True:
    try:

        [ok, frame] = cap.read()          #   Read one frame       
         
        if saved_options != []:
            frame = apply_presaved(frame)
        
        end_img = apply(frame, box, shift)                
        
        end_img = cv2.flip(end_img, 1)
        show_img = cv2.cvtColor(end_img, cv2.COLOR_BGR2RGB)
        show_img = Image.fromarray(show_img)
        show_img= ImageTk.PhotoImage(image = show_img) 
        Canvas.create_image(0, 0, anchor = Tk.NW,  image = show_img)
    
    
        key = cv2.waitKey(1)
        if key == ord('p'):
            cv2.imwrite('save.jpg', end_img)
        if key == ord('q'):
            break
        
        top.update()
    
    except:
        print(sys.exc_info()) 
        cap.release()
        cv2.destroyAllWindows()
        top.quit()
        top.destroy()

