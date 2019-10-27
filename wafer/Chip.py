'''
Created on 4 oct. 2019

@author: DavidS
'''
from Shapes import Shape


class Chip(Shape):
    '''
    classdocs
    '''
    
    def __init__(self,x,y,colour, width=1000, height=1000, enabled=False, isBlank=False):

        Shape(Chip, self).__init__(x, y, colour)
        self.__width = width
        self.__height = height
        self.__enabled = enabled
        self.__isBlank = isBlank

    def get_visited(self):
        return self.__visited


    def get_being_visited(self):
        return self.__beingVisited


    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y


    def get_width(self):
        return self.__width


    def get_height(self):
        return self.__height


    def get_enabled(self):
        return self.__enabled


    def get_is_blank(self):
        return self.__isBlank


    def set_visited(self, value):
        self.__visited = value


    def set_being_visited(self, value):
        self.__beingVisited = value


    def set_x(self, value):
        self.__x = value


    def set_y(self, value):
        self.__y = value


    def set_width(self, value):
        self.__width = value


    def set_height(self, value):
        self.__height = value


    def set_enabled(self, value):
        self.__enabled = value


    def set_is_blank(self, value):
        self.__isBlank = value

    visited = property(get_visited, set_visited, None, None)
    beingVisited = property(get_being_visited, set_being_visited, None, None)
    x = property(get_x, set_x, None, None)
    y = property(get_y, set_y, None, None)
    width = property(get_width, set_width, None, None)
    height = property(get_height, set_height, None, None)
    enabled = property(get_enabled, set_enabled, None, None)
    isBlank = property(get_is_blank, set_is_blank, None, "The chip is mark as Blank for aligment purposes. There is no chip in this place.")

