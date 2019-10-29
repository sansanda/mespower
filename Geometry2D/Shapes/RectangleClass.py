'''
Created on 4 oct. 2019

@author: DavidS
'''

from Geometry2D.Shapes.Shape2DClass import Shape2D
from Geometry2D.PointClass import Point
from Geometry2D.LineClass import  Line
from Geometry2D.Shapes.CircleClass import Circle


class Rectangle(Shape2D):
    '''
    classdocs
    '''
    # initialPoint (left,bottom corner)
    # finalPoint   (Rigth,upper corner)
    # basePoint    (Rigth,bottom corner)
    # dimensions in millimeters (width and height)

    def __init__(self,originPoint,colour,width=1000,height=1000):
        super().__init__(originPoint,colour,width,height)


    #methods for transformations to others shapes

    def getAsCenteredCircle(self, diameter=None):
        c = Circle()
        c.move(self.getCenterPoint()) #circle is centered on x,y shape
        if not diameter: c.setDiameter(self.getHeight()) #return shape as circle with diameter = height
        return c

    def collides(self,shape):
        return

    def getRealArea(self):
        return

    def __str__(self):
        return

def main():
    rec1 = Rectangle(Point(2, 2),'black',500,500)

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
    line1 = rec1.getDiagonalLine()
    print(line1)
    print(line1.getAngle())

    line2 = Line(Point(0,0),Point(-2,10))
    print('line1 Angle = ',line1.getAngle())
    print('line2 Angle = ',line2.getAngle())
    print('Angle Between Lines 1 and 2 = ',Line.getLinesAngle(line1,line2))

    rec2 = Rectangle(Point(2, 2),None,500,1000)
    print(rec2.getBaseLine())
    print(rec2.getBaseLine().getAngle())
    print(rec2.collides(line2))


if __name__ == '__main__':
    main()
