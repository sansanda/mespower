'''
Created on 29 oct. 2019

@author: DavidS
'''


from Geometry2D.Shapes.Shape2DClass import Shape2D
from Geometry2D.PointClass import Point


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
    rec1 = Rectangle(Point(2, 2),None,500,500)
    print(rec1.getArea())
    print(rec1.getOriginPoint())
    print(rec1.getCenterPoint())
    print(rec1.getFinalDiagonalPoint())

    rec1.move(Point(4, 4))
    print(rec1.getArea())
    print(rec1.getCenterPoint())
    print(rec1.getDiagonalLine())
    rec1.scale(2.0)
    print(rec1.getCenterPoint())
    print(rec1.getArea())
    print(rec1.getDiagonalLine())

    rec2 = Rectangle(Point(2, 2),None,500,1000)
    print(rec2.getBaseLine())
    print(rec2.getBaseLine().getAngle())


if __name__ == '__main__':
    main()
