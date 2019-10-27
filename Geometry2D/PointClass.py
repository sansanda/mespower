class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, otherPoint):
        """Overrides the default implementation"""
        if isinstance(otherPoint, Point):
            return (self.getX() == otherPoint.getX()) & (self.getY() == otherPoint.getY())
        return False

