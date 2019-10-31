'''
Created on 9 oct. 2019

@author: DavidS
'''
from Geometry2D.PointClass import Point
from Geometry2D.LineClass import Line
import math

class Shape2D():
    
    # x is left origin
    # y is lower origin
    # dimensions in millimeters

    #private

    def __init__(self,originPoint=Point(0,0),colour='black',width=1000,height=1000):
        self.__originPoint = originPoint
        self.__colour = colour
        self.__width = width
        self.__height = height
        self.__centerPoint = Point(self.__originPoint.getX()+self.__width/2,self.__originPoint.getY()+self.__height/2)
        self.__finalDiagonalPoint = Point(self.__originPoint.getX() + self.__width, self.__originPoint.getY() + self.__height)
        self.__finalBasePoint = Point(self.__originPoint.getX()+self.__width,self.__originPoint.getY()+0)
        self.__diagonalLine = Line(self.__originPoint,self.__finalDiagonalPoint)
        self.__baseLine = Line(self.__originPoint,self.__finalBasePoint)

    def update(self):

        #update points
        self.__updateCenterPoint()
        self.__updateFinalDiagonalPoint()
        self.__updateFinalBasePoint()

        #update lines
        self.__updateDiagonalLine()
        self.__updateBaseLine()

    def __updateCenterPoint(self):
        self.__centerPoint = Point(self.__originPoint.getX()+self.__width/2,self.__originPoint.getY()+self.__height/2)

    def __updateFinalBasePoint(self):
        self.__finalBasePoint = Point(self.__originPoint.getX()+self.__width,self.__originPoint.getY()+0)

    def __updateFinalDiagonalPoint(self):
        self.__finalDiagonalPoint = Point(self.__originPoint.getX() + self.__width, self.__originPoint.getY() + self.__height)

    def __updateDiagonalLine(self):
        self.__diagonalLine = Line(self.__originPoint, self.__finalDiagonalPoint)

    def __updateBaseLine(self):
        self.__baseLine = Line(self.__originPoint,self.__finalBasePoint)

    #public methods

    # get dimensions

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    #get lines of shape

    def getDiagonalLine(self):
        return self.__diagonalLine

    def getBaseLine(self):
        return self.__baseLine

    #get points of shape

    def getOriginPoint(self):
        return self.__originPoint

    def getCenterPoint(self):
        return self.__centerPoint

    def getFinalDiagonalPoint(self):
        return self.__finalDiagonalPoint

    def getFinalBasePoint(self):
        return self.__finalBasePoint

    # get areas
    def getArea(self):
        return (self.__width*self.__height)

    def setColor(self, newColor):
        self.__colour = newColor
        self.update()

    def move(self,newPoint):
        self.__originPoint = newPoint
        self.update()

    def setWidth(self, newWidth):
        self.__width = newWidth
        self.update()

    def setHeight(self, newHeight):
        self.__height = newHeight
        self.update()

    def scale(self, factor):
        self.scaleHorizontally(factor)
        self.scaleVertically(factor)

    def scaleVertically(self, factor):
        self.__height *= factor
        self.update()

    def scaleHorizontally(self, factor):
        self.__width *= factor
        self.update()


    #It is based on widht and height, so it not takes into account irregular forms like polygons
    def __eq__(self, otherShape2D, rel_tol=1e-06, abs_tol=0.0):
        """Overrides the default implementation"""
        if isinstance(otherShape2D, Shape2D):
            return ((self.getCenterPoint()==otherShape2D.getCenterPoint()) &
                    math.isclose(self.getWidth(),otherShape2D.getWidth(),rel_tol=rel_tol, abs_tol=abs_tol) &
                    math.isclose(self.getHeight(),otherShape2D.getHeight(),rel_tol=rel_tol, abs_tol=abs_tol)
                    )
        return False

    #abstract methods
    def collides(self,shape):
        raise NotImplementedError

    def getRealArea(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

