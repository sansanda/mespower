'''
Created on 9 oct. 2019

@author: DavidS
'''
import abc


class Shape(metaclass=abc.ABCMeta):        
    
    # x is left origin
    # y is lower origin
    
    def __init__(self, x=0, y=0, colour=None):
        self.x = x 
        self.y = y
        self.colour = colour
    
    def move(self,x,y):
        self.x = x 
        self.y = y
    
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