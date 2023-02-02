from tkinter import *
from tkinter import ttk, Label
from PIL import Image, ImageDraw, ImageTk, ImageFont


def _r(x,y,z,w,k):
    y.destroy()
    globals()['F%s' % x]=Frame(k)
    globals()['F%s' % x].pack()
    from R import daily_routine,layout
    layout(globals()['F%s' % x])
    daily_routine(globals()['F%s' % x],x,z,w,k)
    for child in globals()['F%s' % x].winfo_children():
        child.grid_configure(padx=10, pady=10)
