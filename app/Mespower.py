#!/usr/bin/env python
"""
Code illustration: 3.02
Drum Program Editor Code
Setting up Widgets


@Tkinter GUI Application Development Hotshot
"""

from tkinter import *


#constants

MAX_DRUM_NUM = 5
MAX_BEAT_PATTERN_NUM = 40

class Mespower():

    def create_main_frame(self):
        self.main_frame = Frame(self.root, height=15)
        self.main_frame.grid(row=0,column=0,padx=10, pady=10)

    def create_top_frame(self):
        top_frame = Frame(self.main_frame, height=15)
        ln = MAX_DRUM_NUM+10
        top_frame.grid(row=ln, columnspan=13,sticky=W+E,padx=15, pady=10)



    def create_left_frame(self):
        left_frame = Frame(self.main_frame)
        left_frame.grid(row=10, column=0, columnspan=6,sticky=W+E+N+S)


    def create_right_frame(self):
        right_frame = Frame(self.main_frame)
        right_frame.grid(row=10, column=6,sticky=W+E+N+S, padx=15, pady=2)


    def create_top_bar(self):
        '''creating top buttons'''
        topbar_frame = Frame(self.main_frame)
        topbar_frame.config(height=25)
        topbar_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5)

        Label(topbar_frame, text='Units:').grid(row=0, column=4)
        self.units = IntVar()
        self.units.set(4)
        self.units_widget = Spinbox(topbar_frame, from_=1, to=8, width=5, textvariable=self.units)
        self.units_widget.grid(row=0, column=5)

        Label(topbar_frame, text='BPUs:').grid(row=0, column=6)
        self.bpu = IntVar()
        self.bpu.set(4)
        self.bpu_widget = Spinbox(topbar_frame, from_=1, to=10, width=5, textvariable=self.bpu)
        self.bpu_widget.grid(row=0, column=7)





    def app(self):
        self.root = Tk()
        self.root.title('Wafer Stage')
        self.create_main_frame()
        self.create_top_bar()
        self.create_left_frame()
        self.create_right_frame()
        self.create_top_frame()
        self.root.mainloop()


# ======================================================================
if __name__ == '__main__':

    mp = Mespower()
    mp.app()
