# -*- coding: utf-8 -*-
"""
tkinter components and functions
"""

import tkinter as Tk
import tkinter.ttk as ttk
#from PIL import Image
#from PIL import ImageTk
import numpy as np
import fun_light
import fun_color
import fun_detail

def initGUI ():
    top = Tk.Tk()
    top.geometry("960x720")
    top.title('Have Fun')
    
#    style = ttk.Style()
    
#    global detail_shift 
    detail_shift = Tk.IntVar()
    detail_shift.set(0)
#    global light_shift
    light_shift = Tk.IntVar()
    light_shift.set(0)
#    global color_shift
    color_shift= Tk.IntVar()
    color_shift.set(0)
#    global HSL_shift
    HSL_shift= Tk.IntVar()
    HSL_shift.set(0)
    global saved_options
    saved_options = []
    
#    Canvas  = Tk.Label(top, image = None) 
    Canvas = Tk.Canvas(top, width = 640, height = 480)
    S_detail = Tk.Scale(top, variable = detail_shift, from_ = 0, to = 10)
    S_light  = Tk.Scale(top, variable = light_shift, from_ = -10, to = 10)
    S_color  = Tk.Scale(top, variable = color_shift, from_ = -10, to = 10)
    S_HSL    = Tk.Scale(top, variable = HSL_shift, from_ = -20, to = 20)
    L_color  = Tk.Label(top, text = 'Color', font = ("arial", 12))
    L_detail = Tk.Label(top, text = 'Detail', font = ("arial", 12))
    L_light  = Tk.Label(top, text = 'Light', font = ("arial", 12))
    L_HSL    = Tk.Label(top, text = 'HSL', font = ("arial", 12))
    C_color  = ttk.Combobox(top, width = 10, values = ('', 
                                                       'hue', 
                                                       'saturation', 
                                                       'luminance'))
    C_detail = ttk.Combobox(top, width = 10, values = ('',
                                                       'sharpen',
                                                       'blur',
                                                       'denoise',
                                                       'edge'))
    C_light  = ttk.Combobox(top, width = 10, values = ('', 
                                                       'brightness',
                                                       'contrast',
                                                       'highlight',
                                                       'shadows', 
                                                       'white levels',
                                                       'black levels'))
    C_HSL    = ttk.Combobox(top, width = 10, values = ('', 'red','blue',
                                                       'green', 'orange',
                                                       'yellow', 'cyan'))
    B_filt1 = Tk.Button(top, text = 'Old Photo', font = ("arial", 12))
    B_filt2 = Tk.Button(top, text = 'Vivid', font = ("arial", 12))
    B_filt3 = Tk.Button(top, text = 'Fade', font = ("arial", 12))
    B_shoot = Tk.Button(top, text = 'SHOOT', font = ("arial", 12))
    B_reset = Tk.Button(top, text = 'RESET', font = ("arial", 12))
#    global B_compare
    B_apply = Tk.Button(top, text = 'APPLY', font = ("arial", 12))
    
    Canvas.place(x = 15, y = 15, width = 640, height = 480)
    L_detail.place(x = 25, y = 510)
    L_light.place(x = 25 + 160, y = 510)
    L_HSL.place(x = 25 + 160 * 2, y = 510)
    L_color.place(x = 25 + 160 * 3, y = 510)
    C_detail.place(x = 15, y = 550)
    C_light.place(x = 15 + 160, y = 550)
    C_color.place(x = 15 + 160 * 2, y = 550)
    C_HSL.place(x = 15 + 160 * 3, y = 550)
    S_detail.place(x = 15, y = 590) 
    S_light.place(x = 15 + 160, y = 590)
    S_color.place(x = 15 + 160 * 2, y = 590)
    S_HSL.place(x = 15 + 160 * 3, y = 590)
    B_filt1.place(x = 15 + 640 + 50, y = 25 + 120, width = 200, height = 80)
    B_filt2.place(x = 15 + 640 + 50, y = 25, width = 200, height = 80)
    B_filt3.place(x = 15 + 640 + 50, y = 25 + 120 * 2, width = 200, height = 80)
    B_shoot.place(x = 15 + 640 + 108, y = 610, width = 140, height = 80) 
    B_reset.place(x = 15 + 640 + 108, y = 510, width = 140, height = 80)
    B_apply.place(x = 15 + 640 + 108, y = 410, width = 140, height = 80)
   
    box = (C_detail, C_light, C_color, C_HSL)
    shift = (detail_shift, light_shift, color_shift, HSL_shift)
    buttons = (B_apply, B_reset, B_shoot, B_filt1, B_filt2, B_filt3)
    
    buttons[0].configure(command = lambda: apply_get(shift, box))
    buttons[1].configure(command = lambda: reset(shift))
    buttons[3].configure(command = filter1)
    buttons[4].configure(command = filter2)
    buttons[5].configure(command = filter3)
    
    return top, Canvas, box, shift, saved_options, buttons[2]

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
    return end_img

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
    
def filter1(): # 'old photo'
    global saved_options
    saved_options.append([0, 'sharpen', 4])
    saved_options.append([1, 'highlight', 10])
    saved_options.append([2, 'hue', 3])
    saved_options.append([1, 'white levels', 5])
    saved_options.append([0, 'denoise', 1])
    saved_options.append([2, 'saturation', 5])
#    saved_options.append([3, 'hue', 8, 'orange'])
    saved_options.append([3, 'hue', -9, 'blue'])

def filter2(): # 'vivid'
    global saved_options
    saved_options.append([2, 'saturation', 4])
    saved_options.append([1, 'brightness', 3]) 
    saved_options.append([1, 'contrast', 10])
    saved_options.append([1, 'highlight', 7])
    saved_options.append([1, 'white levels', 6])
    saved_options.append([1, 'black levels', -1])
    
def filter3():  # 'fade'
    global saved_options
    saved_options.append([2, 'saturation', -30])
    saved_options.append([1, 'contrast', 8])
    saved_options.append([1, 'shadows', 3])
    saved_options.append([1, 'white levels', 2])
    saved_options.append([1, 'black levels', -4])
    saved_options.append([0, 'sharpen', 1])
    saved_options.append([3, 'saturation', -20, 'red'])
    saved_options.append([3, 'saturation', -20, 'blue'])
    
    