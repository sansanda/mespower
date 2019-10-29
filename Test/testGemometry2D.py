import unittest
from Geometry2D.LineClass import Line
from Geometry2D.PointClass import Point

class TestLineMethods(unittest.TestCase):

    line = Line(Point(2, 2), Point(1, 4))
    line2 = Line(Point(2, 2), Point(4, 4))
    line3 = Line(Point(0, 0), Point(0, 4))
    line4 = Line(Point(0, 0), Point(0, 4))
    line5 = Line(Point(0, 0), Point(0, -4))
    line6 = Line(Point(0, 0), Point(10, -4))
    line7 = Line(Point(0, 0), Point(0, 1))


    def test_slope(self):
        pass
        self.assertEqual(self.line.getSlope(), -2.0)
        self.assertEqual(self.line2.getSlope(), 1.0)
        self.assertEqual(self.line3.getSlope(), None)
        self.assertEqual(self.line4.getSlope(), None)


    def test_angle(self):

        self.assertAlmostEqual(self.line.getAngle(), 116.565,3)
        self.assertEqual(self.line2.getAngle(),45.0)
        self.assertEqual(self.line3.getAngle(), 90.0)
        self.assertEqual(self.line4.getAngle(), 90.0)
        self.assertEqual(self.line5.getAngle(), 270.0)
        self.assertAlmostEqual(self.line6.getAngle(), 338.198,2)
        self.assertEqual(self.line7.getAngle(), 90.0)


if __name__ == '__main__':
    unittest.main()
