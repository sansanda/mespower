'''
Created on 4 oct. 2019

@author: DavidS
'''

from wafer import Shape

class WaferCell(Shape):
    '''
    classdocs
    '''

    def __init__(self,x,y,colour,width=1000,height=1000,enabled=False, isBlank=False, chipsArray=None):
    
        Shape(WaferCell,self).__init__(x, y, colour)
        self.__width = width
        self.__height = height
        self.__enabled = enabled
        self.__isBlank = isBlank
        self.__chipsArray = chipsArray
        