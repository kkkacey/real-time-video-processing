# -*- coding: utf-8 -*-
"""
"""

import sys
#import numpy as np 
import cv2
import tkinter as Tk 
from PIL import Image
from PIL import ImageTk

import fun_detail
import fun_GUI
import fun_color
import fun_light

top, Canvas, shift = fun_GUI.initGUI()

cap = cv2.VideoCapture(0)

while True:
    try:

        [ok, frame] = cap.read()          #   Read one frame
        
        end_img = fun_detail.sharpen_and_blur(frame, shift[1].get())
        
        end_img = fun_color.saturation(end_img, shift[0].get())
        
        end_img = fun_light.contrast(end_img, shift[2].get())
        
        end_img = fun_color.color_hue(end_img, 'blue', shift[3].get())
        
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
#        print(sys.exc_info()[0]) 
        cap.release()
        cv2.destroyAllWindows()
        top.quit()
        top.destroy()
                


