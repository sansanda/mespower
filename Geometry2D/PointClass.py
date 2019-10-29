import math

class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def collides(self,shape):
        return self==shape

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, otherPoint, rel_tol=1e-06, abs_tol=0.0):
        """Overrides the default implementation"""
        if isinstance(otherPoint, Point):
            return (math.isclose(self.getX(),otherPoint.getX(),rel_tol=rel_tol, abs_tol=abs_tol) & math.isclose(self.getY(),otherPoint.getY(),rel_tol=rel_tol, abs_tol=abs_tol))
        return False

def main():
    p1 = Point(1.000001,1.0)
    p2 = Point(1.0,1.0)
    print(p1==p2)
    print(p1.getY())


if __name__ == '__main__':
    main()