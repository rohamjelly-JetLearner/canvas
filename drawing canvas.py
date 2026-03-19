from tkinter import *
from tkinter.colorchooser import askcolor

root=Tk()

oldx=0
oldy=0
def activate_button(button,erasermode=False):
    global eraser_on,active_button
    active_button.config(relief=RAISED)
    button.config(relief=SUNKEN)
    active_button=button
    eraser_on=erasermode

def eraser_active():
    activate_button(eraser,erasermode=True)

def colour_change():
    global eraser_on,color
    eraser_on=False
    color=askcolor(color)[1]

def brush_draw():
    activate_button(brush)

def pen_draw():
    activate_button(pen)

eraser_on=False
color='black'
pen=Button(root,text='PEN',command=pen_draw)
pen.grid(column=0,row=0)
brush=Button(root,text='BRUSH',command=brush_draw)
brush.grid(column=1,row=0)
colour=Button(root,text='COLOUR',command=colour_change)
colour.grid(column=2,row=0)
eraser=Button(root,text='ERASER',command=eraser_active)
eraser.grid(column=3,row=0)
pen=Scale(root,from_=1 ,to=10,orient=HORIZONTAL)
pen.grid(column=4,row=0)
canvas=Canvas(root,bg='white')
canvas.grid(columnspan=5,row=1)
active_button=pen

root.mainloop()