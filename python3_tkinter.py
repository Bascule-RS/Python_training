import tkinter as tk
import random
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import time


    
def _from_rgb():
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % (random.randrange(0,250),random.randrange(0,250),random.randrange(0,250)) 

        

        
root = Tk()
root.geometry("400x250+300+300")

canvas = Canvas()

#etoile = Label(root, text='*',fg=_from_rgb())
#zone = Canvas(root, width=200, height =150, bg ="white")
#zone.pack()
def dessine():
    x = random.randrange(0,400)
    y = random.randrange(0,250)
    r= random.randrange(0,10)
    
    canvas.create_oval(x-r,y-r,x+r,y+r, fill=_from_rgb(),outline="")       
    canvas.pack(fill=BOTH, expand=1)

for i in range(9999):
    dessine()

 # Create a text label
 # Pack it into the window

#Image = PhotoImage(filename = [Your Image here])

# Lbl = Label (width=490, img=image)

#for i in range(0,3):
#    col = random.randrange(0,3)
#    row = random.randrange(0,3)
#    etoile.grid =col
#    etoile.grid
#    etoile.pack()
#    labelrouge = Text(root)
#   labelrouge.insert(INSERT,"*")
#    labelrouge.grid = col
#    labelrouge.grid = row
#    labelrouge.pack
#    labelrouge.pack(padx=1, pady=1)
root.mainloop()