'''
Created on 4 oct. 2019

@author: DavidS
'''

from Geometry2D.ShapeClass import Shape
from Geometry2D.PointClass import Point
import abc

class Rectangle(Shape):
    '''
    classdocs
    '''
    # initialPoint of te diagonal (left,bottom corner)
    # finalPoint of te diagonal (Rigth,upper corner)

    def __init__(self,originPoint,colour,width=1000,height=1000):

        Shape(Rectangle, self).__init__(originPoint, colour)
        self.__width = width
        self.__height = height
        self.__centerPoint = Point(self.__originPoint.getX()+width/2,self.__originPoint.getY()+height/2)


    def collides(self, shape):
        return

    def scaleVertically(self, factor):
        return

    def scaleHorizontally(self, factor):
        return

    def getArea(self):
        return

    def __str__(self):
        return

def main():
    rec1 = Rectangle(Point(2, 2),None)

if __name__ == '__main__':
    main()