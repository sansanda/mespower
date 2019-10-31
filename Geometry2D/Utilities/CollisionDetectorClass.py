from Geometry2D.PointClass import Point
from Geometry2D.LineClass import Line
from Geometry2D.Shapes.CircleClass import Circle
from Geometry2D.Shapes.RectangleClass import Rectangle

class CollisionDetector():
    '''
    classdocs
    '''
    #Collision Detector is a pure static class with only static methods
    #whith the sole purpose of detecting the collision of diferent shapes

    @classmethod
    def collides(cls,shape1,shape2):
        collides = False

        if isinstance(shape1,Point):
            if isinstance(shape2, Line):
                pass

        if isinstance(shape1, Line):
            pass

        if isinstance(shape1, Circle):
            pass

        if isinstance(shape1, Rectangle):
            pass

        return collides
