from tkinter import *
from PIL import Image, ImageTk

def check_collision(canvas, circleID, rectangleCoords):
    collides = False
    canvas.itemconfig(circleID,fill='white')
    result = canvas.find_overlapping(*rectangleCoords)

    for i in result:
        if i == circleID:
            collides = True
    canvas.itemconfig(circleID,fill='')
    return collides




wafer_diameter = 100*4

chip_height = 20
chip_width = 20

canvas_width_offset = chip_width*5
canvas_height_offset = chip_height*5

canvas_width = wafer_diameter + canvas_width_offset
canvas_height = wafer_diameter + canvas_height_offset

nChipsPerRow = int(canvas_width/chip_width)
nChipsPerColumn = int(canvas_width/chip_height)

wafer_center_x = canvas_width/2
wafer_center_y = canvas_height/2

master = Tk()
master.geometry(str(int(canvas_width))+"x"+str(int(canvas_height))) #You want the size of the app to be 500x500
master.resizable(0, 0) #Don't allow resizing in the x or y direction
master.update()


canvas = Canvas(master,width=canvas_width,height=canvas_height)
canvas.update()
canvas.pack()
canvas.place(bordermode=INSIDE, x=0, y=0)



waferCircleID = canvas.create_oval(wafer_center_x - (wafer_diameter / 2),
                                   wafer_center_y - (wafer_diameter / 2),
                                   wafer_center_x + (wafer_diameter / 2),
                                   wafer_center_y + (wafer_diameter / 2))


chipsIDArray = [[0] * nChipsPerColumn] * nChipsPerRow

for x in range(nChipsPerRow):
    for y in range(nChipsPerColumn):
        rectangleCoords = (x * chip_width, y * chip_height, x * chip_width + chip_width, y * chip_height + chip_height)
        rectangleColor = 'red'
        if check_collision(canvas, waferCircleID, rectangleCoords):
            rectangleColor = 'blue'
        chipsIDArray[y][x] = canvas.create_rectangle(rectangleCoords, fill=rectangleColor)

canvas.tag_raise(waferCircleID)




mainloop()
