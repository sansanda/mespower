'''
Created on 9 oct. 2019

@author: DavidS
'''
import abc

class Shape(metaclass=abc.ABCMeta):        
    
    # x is left origin
    # y is lower origin
    
    def __init__(self, originPoint, colour=None):
        self.__originPoint = originPoint
        self.__colour = colour
    
    def move(self,newPoint):
        self.__originPoint = newPoint
    
    def scale(self, factor):
        self.scaleHorizontally(factor)
        self.scaleVertically(factor)
    
    @abc.abstractmethod
    def collides(self,shape):
        return
        
    @abc.abstractmethod
    def scaleVertically(self, factor):
        return
    
    @abc.abstractmethod
    def scaleHorizontally(self, factor):
        return
    
    @abc.abstractmethod
    def getArea(self):
        return
    
    @abc.abstractmethod
    def __str__(self):
        return