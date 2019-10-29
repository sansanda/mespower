from Geometry2D.PointClass import Point

import math

class Line:

    @classmethod
    def getLineAngle(cls,line):

        deltaX = line.__finalPoint.getX()-line.__originPoint.getX()
        deltaY = line.__finalPoint.getY()-line.__originPoint.getY()

        try:
            angle = atanInDegrees = math.degrees(math.atan(deltaY/deltaX))
            #print(deltaX, deltaY,math.degrees(math.atan(deltaY/deltaX)))
            if (deltaX < 0) & ((deltaY >= 0) or (deltaY <= 0)):
                angle = atanInDegrees + 180.0
            if (deltaX > 0) & (deltaY < 0):
                angle = atanInDegrees + 360.0
        except ZeroDivisionError:
            if (deltaY>0): angle = 90.0
            else: angle  = 270.0
        return angle

    @classmethod
    def getLinesAngle(cls,line1,line2):

        angleLine1 = cls.getLineAngle(line1)
        angleLine2 = cls.getLineAngle(line2)
        return math.fabs(angleLine1-angleLine2)


    def __init__(self, originPoint, finalPoint):
        if (originPoint==finalPoint): raise Exception('PointsEquals', 'Points cannot be equals in line definition')
        self.__originPoint = originPoint
        self.__finalPoint = finalPoint

    def getOriginPoint(self):
        return self.__originPoint

    def getFinalPoint(self):
        return self.__finalPoint

    def getSlope(self):
        try:
            return (self.getFinalPoint().getY() - self.getOriginPoint().getY()) / (self.getFinalPoint().getX() - self.getOriginPoint().getX())
        except ZeroDivisionError:
            return None

    def getYAxisCrossPoint(self):
        if self.getSlope()==None: return None
        return Point(0,self.getOriginPoint().getY() - (self.getOriginPoint().getX() * self.getSlope()))

    def getAngle(self):
        return Line.getLineAngle(self)

    def collides(self,shape):
        return self==shape

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, otherLine, rel_tol=1e-06, abs_tol=0.0):
        """Overrides the default implementation"""
        equals = False
        if isinstance(otherLine, Line):
            if ((self.getSlope() == None) & (otherLine.getSlope() == None)): equals = True
            elif ((not self.getSlope()) & (not otherLine.getSlope())):
                equals = (self.getYAxisCrossPoint()==otherLine.getYAxisCrossPoint()) & math.isclose(self.getSlope(),otherLine.getSlope(),rel_tol=rel_tol, abs_tol=abs_tol)
        return equals

def main():
    line = Line(Point(2, 2), Point(1, 4))
    line2 = Line(Point(2, 2), Point(4, 4))
    line3 = Line(Point(0, 0), Point(0, 4))
    line4 = Line(Point(0, 0), Point(0, 4))
    line5 = Line(Point(0, 0), Point(0, -4))
    line6 = Line(Point(0, 0), Point(10, -4))
    line7 = Line(Point(0, 0), Point(0, 1))
    line8 = Line(Point(0, 0), Point(5, 5))
    line9 = Line(Point(0,0) , Point(10,10))

    print(line.getAngle())
    print(line2.getAngle())
    print(line3.getAngle())
    print(line4.getAngle())
    print(line5.getAngle())
    print(line6.getAngle())
    print(line7.getAngle())

    print(line == line2)
    print(line3.collides(line4))

    print(line3.getSlope())
    print(line9.getYAxisCrossPoint())

if __name__ == '__main__':
    main()
