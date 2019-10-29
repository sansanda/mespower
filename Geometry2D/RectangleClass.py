'''
Created on 4 oct. 2019

@author: DavidS
'''

from Geometry2D.Shape2DClass import Shape2D
from Geometry2D.PointClass import Point
import abc

class Rectangle(Shape2D):
    '''
    classdocs
    '''
    # initialPoint of te diagonal (left,bottom corner)
    # finalPoint of te diagonal (Rigth,upper corner)

    def __init__(self,originPoint,colour,width=1000,height=1000):
        super().__init__(originPoint,colour,width,height)


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
    print(rec1.getFinalPoint())

    rec1.move(Point(4, 4))
    print(rec1.getArea())
    print(rec1.getCenterPoint())
    print(rec1.getDiagonalLine())
    rec1.scale(2.0)
    print(rec1.getCenterPoint())
    print(rec1.getArea())
    print(rec1.getDiagonalLine())

    rec2 = Rectangle(Point(2, 2),None,500,1000)
    print(rec2.getDiagonalLine().getAngle())


if __name__ == '__main__':
    main()
