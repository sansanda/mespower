'''
Created on 29 oct. 2019

@author: DavidS
'''


from Geometry2D.Shapes.Shape2DClass import Shape2D
from Geometry2D.PointClass import Point

import math

class Circle(Shape2D):
    '''
    classdocs
    '''

    # dimensions in millimeters

    def __init__(self,originPoint,colour,diameter=101.6):
        super().__init__(originPoint,colour,diameter,diameter)
        self.__diameter = diameter

    def getDiameter(self):
        return self.__diameter

    def setDiameter(self, newDiameter):
        self.__diameter = newDiameter
        super().setHeight(newDiameter)
        super().setWidth(newDiameter)

    def collides(self, shape):
        return

    def getRealArea(self):
        return

    def __str__(self):
        return

def main():
    circ1 = Circle(Point(2, 2),'black',500)
    circ2 = Circle(Point(2, 2),'black',500)
    circ3 = Circle(Point(2, 2),'black',600)
    circ4 = Circle(Point(1, 2),'black',500)

    print(circ1==circ2)
    print(circ2==circ3)
    print(circ2==circ4)
    print(circ3==circ4)
    print(circ4==circ4)

if __name__ == '__main__':
    main()
