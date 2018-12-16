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

#import fun_detail
import fun_GUI
#import fun_color
#import fun_light

def shoot(end_img):
    import time
    localtime = time.localtime()[0:5]
    timestr = str(localtime[0])[2:4]
    for i in range(1,5):
        timestr += str(localtime[i])
        if i == 2:
            timestr += '_'
    cv2.imwrite('photoshot' + timestr + '.jpg', end_img)
    print('photoshot saved.')

top, Canvas, box, shift, saved_options, B_shoot = fun_GUI.initGUI()

cap = cv2.VideoCapture(0)

while True:
    try:

        [ok, frame] = cap.read()          #   Read one frame       
        
        if fun_GUI.saved_options != []:
            frame = fun_GUI.apply_presaved(frame)
        
        end_img = fun_GUI.apply(frame, box, shift)                
        
        end_img = cv2.flip(end_img, 1)
        show_img = cv2.cvtColor(end_img, cv2.COLOR_BGR2RGB)
        show_img = Image.fromarray(show_img)
        show_img= ImageTk.PhotoImage(image = show_img) 
        Canvas.create_image(0, 0, anchor = Tk.NW,  image = show_img)
    
        B_shoot.configure(command = lambda: shoot(end_img))
        
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