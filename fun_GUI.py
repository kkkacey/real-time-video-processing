# -*- coding: utf-8 -*-
"""
tkinter components and functions
"""

import tkinter as Tk
import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk
import cv2

def initGUI ():
    top = Tk.Tk()
    top.geometry("960x720")
    
#    style = ttk.Style()
    
    global detail_shift 
    detail_shift = Tk.IntVar()
    detail_shift.set(0)
    global light_shift
    light_shift = Tk.IntVar()
    light_shift.set(0)
    global color_shift
    color_shift= Tk.IntVar()
    color_shift.set(0)
    global HSL_shift
    HSL_shift= Tk.IntVar()
    HSL_shift.set(0)
    
#    Canvas  = Tk.Label(top, image = None) 
    Canvas = Tk.Canvas(top, width = 640, height = 480)
    S_detail = Tk.Scale(top, variable = detail_shift, from_ = 0, to = 10)
    S_light  = Tk.Scale(top, variable = light_shift, from_ = -10, to = 10)
    S_color  = Tk.Scale(top, variable = color_shift, from_ = -10, to = 10)
    S_HSL    = Tk.Scale(top, variable = HSL_shift, from_ = -255, to = 255)
    L_color  = Tk.Label(top, text = 'color', font = ("arial", 12))
    L_detail = Tk.Label(top, text = 'detail', font = ("arial", 12))
    L_light  = Tk.Label(top, text = 'light', font = ("arial", 12))
    L_HSL    = Tk.Label(top, text = 'HSL', font = ("arial", 12))
    C_color  = ttk.Combobox(top, width = 10, values = ('hue', 'saturation', 'luminance'))
    C_detail = ttk.Combobox(top, width = 10, values = ('sharpen', 'blur', 'denoise'))
    C_light  = ttk.Combobox(top, width = 10, values = ('brightness', 'contrast'))
    C_HSL    = ttk.Combobox(top, width = 10, values = ('red','blue', 'green', 'yellow', 'cyan', 'magenta'))
    B_filt1 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt2 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt3 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt4 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_reset = Tk.Button(top, text = 'RESET', font = ("arial", 12))
#    global B_compare
    B_compare = Tk.Button(top, text = 'APPLY', font = ("arial", 12))
    
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
    B_filt1.place(x = 15 + 640 + 50, y = 25, width = 200, height = 80)
    B_filt2.place(x = 15 + 640 + 50, y = 25 + 120, width = 200, height = 80)
    B_filt3.place(x = 15 + 640 + 50, y = 25 + 120 * 2, width = 200, height = 80)
    B_filt4.place(x = 15 + 640 + 50, y = 25 + 120 * 3, width = 200, height = 80)
    B_reset.place(x = 15 + 640 + 108, y = 510, width = 140, height = 80)
    B_compare.place(x = 15 + 640 + 108, y = 610, width = 140, height = 80)
    
    box = (C_detail, C_light, C_color, C_HSL)
    shift = (detail_shift, light_shift, color_shift, HSL_shift)
    
    return top, Canvas, box, shift, B_compare, B_reset

    
    