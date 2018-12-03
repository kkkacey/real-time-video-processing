# -*- coding: utf-8 -*-
"""
tkinter components and functions
"""

import tkinter as Tk
from PIL import Image
from PIL import ImageTk
import cv2

def initGUI ():
    top = Tk.Tk()
    top.geometry("960x720")
    
    detail_shift = Tk.IntVar()
    detail_shift.set(0)
    light_shift = Tk.IntVar()
    light_shift.set(0)
    color_shift = Tk.IntVar()
    color_shift.set(0)
    HSL_shift = Tk.IntVar()
    HSL_shift.set(0)
    
#    Canvas  = Tk.Label(top, image = None) 
    Canvas = Tk.Canvas(top, width = 640, height = 480)
    S_detail = Tk.Scale(top, variable = detail_shift, from_ = -10, to = 10)
    S_light  = Tk.Scale(top, variable = light_shift, from_ = -10, to = 10)
    S_color  = Tk.Scale(top, variable = color_shift, from_ = -10, to = 10)
    S_HSL    = Tk.Scale(top, variable = HSL_shift, from_ = -30, to = 30)
    L_color  = Tk.Label(top, text = 'color', font=("arial", 13))
    L_detail = Tk.Label(top, text = 'detail', font=("arial", 13))
    L_light  = Tk.Label(top, text = 'light', font=("arial", 13))
    L_HSL    = Tk.Label(top, text = 'HSL', font=("arial", 13))
    # TODO: 还有一些下拉菜单，形式位置待定
    B_filt1 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt2 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt3 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_filt4 = Tk.Button(top, text = 'filter name', font = ("arial", 12))
    B_reset = Tk.Button(top, text = 'RESET', font = ("arial", 12))
    B_compare = Tk.Button(top, text = 'COMPARE', font = ("arial", 12))
    
    Canvas.place(x = 15, y = 15, width = 640, height = 480)
    L_color.place(x = 25, y = 510)
    L_detail.place(x = 25 + 160, y = 510)
    L_light.place(x = 25 + 160 * 2, y = 510)
    L_HSL.place(x = 25 + 160 * 3, y = 510)
    S_color.place(x = 15, y = 590) 
    S_light.place(x = 15 + 160, y = 590)
    S_detail.place(x = 15 + 160 * 2, y = 590)
    S_HSL.place(x = 15 + 160 * 3, y = 590)
    B_filt1.place(x = 15 + 640 + 50, y = 25, width = 200, height = 80)
    B_filt2.place(x = 15 + 640 + 50, y = 25 + 120, width = 200, height = 80)
    B_filt3.place(x = 15 + 640 + 50, y = 25 + 120 * 2, width = 200, height = 80)
    B_filt4.place(x = 15 + 640 + 50, y = 25 + 120 * 3, width = 200, height = 80)
    B_reset.place(x = 15 + 640 + 108, y = 510, width = 140, height = 80)
    B_compare.place(x = 15 + 640 + 108, y = 610, width = 140, height = 80)
    
    return top, Canvas, (color_shift, light_shift, detail_shift, HSL_shift)  # 还有下拉菜单的选项