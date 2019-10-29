'''
Created on 9 oct. 2019

@author: DavidS
'''
from Geometry2D.PointClass import Point
from Geometry2D.LineClass import Line

class Shape2D():
    
    # x is left origin
    # y is lower origin


    #private

    def __init__(self,originPoint,colour,width,height):
        self.__originPoint = originPoint
        self.__colour = colour
        self.__width = width
        self.__height = height
        self.__centerPoint = Point(self.__originPoint.getX()+self.__width/2,self.__originPoint.getY()+self.__height/2)
        self.__finalPoint = Point(self.__originPoint.getX()+self.__width,self.__originPoint.getY()+self.__height)
        self.__diagonalLine = Line(self.__originPoint,Point(self.__originPoint.getX()+self.__width,self.__originPoint.getY()+self.__height))

    def __update(self):
        self.__updateCenterPoint()
        self.__updateFinalPoint()
        self.__updateDiagonalLine()

    def __updateCenterPoint(self):
        self.__centerPoint = Point(self.__originPoint.getX()+self.__width/2,self.__originPoint.getY()+self.__height/2)

    def __updateFinalPoint(self):
        self.__finalPoint = Point(self.__originPoint.getX()+self.__width,self.__originPoint.getY()+self.__height)

    def __updateDiagonalLine(self):
         self.__diagonalLine = Line(self.__originPoint,self.__finalPoint)

    #public

    def getDiagonalLine(self):
        return self.__diagonalLine

    def getArea(self):
        return (self.__width*self.__height)

    def getOriginPoint(self):
        return self.__originPoint

    def getCenterPoint(self):
        return self.__centerPoint

    def getFinalPoint(self):
        return self.__finalPoint

    def move(self,newPoint):
        self.__originPoint = newPoint
        self.__update()
    
    def scale(self, factor):
        self.scaleHorizontally(factor)
        self.scaleVertically(factor)

    def scaleVertically(self, factor):
        self.__height *= factor
        self.__update()

    def scaleHorizontally(self, factor):
        self.__width *= factor
        self.__update()

    #abstract methods
    def collides(self,shape):
        raise NotImplementedError

    def getRealArea(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
