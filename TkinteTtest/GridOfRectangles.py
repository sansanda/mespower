import tkinter as tk
from tkinter import *
import numpy as np

class Gui():

    # def callback(event):
    #     # Get rectangle diameters
    #     col_width = c.winfo_width()/COLS
    #     row_height = c.winfo_height()/ROWS
    #     # Calculate column and row number
    #     col = int(event.x//col_width)
    #     row = int(event.y//row_height)
    #     # If the tile is not filled, create a rectangle
    #     if not tiles[row][col]:
    #         tiles[row][col] = c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
    #     # If the tile is filled, delete the rectangle and clear the reference
    #     else:
    #         c.delete(tiles[row][col])
    #         tiles[row][col] = None

    def __init__(self, root, chipWidth, chipHeight, nColumns, nRows, offset):
        self.root=root
        self.entry = tk.Entry(root)
        stvar=tk.StringVar()
        stvar.set("one")


        self.canvas=tk.Canvas(root,
                              width=nColumns * chipWidth + offset,
                              height=nRows * chipHeight + offset,
                              background='white',
                              highlightthickness=1,
                              highlightbackground="black")

        self.canvas.grid(row=0,column=1)
        #self.canvas.bind("<Button-1>", callback)

        frame = Frame(root)
        frame.grid(row=0,column=0, sticky="n")

        self.option=tk.OptionMenu(frame, stvar, "one", "two", "three")
        label1=Label(frame, text="Figure").grid(row=0,column=0, sticky="nw")
        label2=Label(frame, text="X").grid(row=1,column=0, sticky="w")
        label3=Label(frame, text="Y").grid(row=2,column=0, sticky="w")
        self.option.grid(row=0,column=1,sticky="nwe")
        entry = Entry(frame).grid(row = 1,column = 1,sticky = E+ W)
        entry1 = Entry(frame).grid(row = 2,column = 1, sticky = E)
        Button1=Button(frame,text="Draw").grid(row = 3,column = 1, sticky = "we")


        for row in range(0, nRows):
            for column in range(0, nColumns):
                self.canvas.create_rectangle(column*chipWidth+offset/2,                 #x1 left,upper corner
                                             row*chipHeight+offset/2,                   #y1
                                             column*chipWidth + chipWidth + offset/2,   #x2 bottom,right corner
                                             row*chipHeight + chipHeight + offset/2,    #y2
                                             fill="blue",
                                             tag=(column,row))




        #Grid.columnconfigure(self.root,1,weight=1, size=200)

if __name__== '__main__':
    root=tk.Tk()
    canvasOffset = 100
    chipWidth = 100
    chipHeight = 20
    nRows=8
    nColumns=8

    gui=Gui(root, chipWidth, chipHeight, nColumns, nRows, canvasOffset)
    root.mainloop()
