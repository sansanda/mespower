from Geometry2D.LineClass import Line
from Geometry2D.PointClass import Point

def main():
    line = Line(Point(2,2),Point(4,4))
    print(line.__str__())

if __name__ == '__main__':
    main()