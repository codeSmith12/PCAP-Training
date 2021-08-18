import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y


    def getx(self):
        return self.__x

    def gety(self):
        return self.__y


    def distance_from_xy(self, x, y):
        return math.hypot(self.__x, self.__y, x, y)

    def distance_from_point(self, point):
        return math.hypot(self.__x, self.__y, point.getx(), point.gety())

class Triangle():
    def __init__(self, vert1, vert2, vert3):
        self.v1 = vert1
        self.v2 = vert2
        self.v3 = vert3
    def perimeter(self):
        sum = 0

        sum += math.hypot(self.v1.getx(),self.v1.gety(),self.v2.getx(),self.v2.gety())
        sum += math.hypot(self.v2.getx(),self.v2.gety(),self.v3.getx(),self.v3.gety())
        sum += math.hypot(self.v3.getx(),self.v3.gety(),self.v1.getx(),self.v1.gety())

        return sum

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
