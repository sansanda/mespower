# python3
import tkinter as tk
from tkinter.ttk import Separator, Style

# for python2 :
# import Tkinter as tk
# from ttk import Separator

fen = tk.Tk()

leftFrame = tk.Frame(fen, bg="black", width=100, height=100)
# to prevent the frame from adapting to its content :
leftFrame.pack_propagate(False)
leftFrame.grid(column=0, row = 0, pady=5, padx=10, sticky="n")
tk.Label(leftFrame, text="Left frame", fg="white", bg="black", anchor="center", justify="center").pack()

sep = Separator(fen, orient="vertical")
sep.grid(column=1, row=0, sticky="ns")

# edit: To change the color of the separator, you need to use a style
sty = Style(fen)
sty.configure("TSeparator", background="red")

rightFrame= tk.Frame(fen, bg="black", width=100, height=100)
rightFrame.pack_propagate(False)
rightFrame.grid(column=2, row = 0, pady=5, padx=10, sticky="n")
tk.Label(rightFrame, text="Right frame", fg="white", bg="black").pack()

fen.mainloop()
