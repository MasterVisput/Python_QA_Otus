import math


class GeometricalFigure:

    def __init__(self, name=None,
                 a=0,
                 b=0,
                 c=0,
                 h=0,
                 r=0):

        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.r = r

    def get_perimeter(self):
        if self.r != 0:
            perimeter = 2*math.pi*self.r
            return perimeter
        elif self.b + self.c + self.r == 0:
            perimeter = self.a*4
            return perimeter
        elif self.b != 0 and (self.c + self.r) == 0:
            perimeter = 2*(self.a + self.b)
            return perimeter
        elif self.h != 0:
            perimeter = self.a + self.b + self.c
            return perimeter


    def get_area(self):
        if self.r != 0:
            area = math.pi*(self.r**2)
            return area
        elif self.b + self.c + self.r == 0:
            area = self.a**2
            return area
        elif self.b != 0 and (self.c + self.r) == 0:
            area = self.a * self.b
            return area
        elif self.h != 0:
            area = 0.5*self.b*self.h
            return area

    def get_angles(self):
        if self.r != 0:
            angles = 0
            return angles
        elif self.b + self.c + self.r == 0:
            angles = 4
            return angles
        elif self.b != 0 and (self.c + self.r) == 0:
            angles = 4
            return angles
        elif self.h != 0:
            angles = 3
            return angles

    def add_square(self, figure):
        if isinstance(figure, GeometricalFigure):
            return self.get_area() + figure.get_area()
        else:
            return 'Переданный объект не является экземпляром класса GeometricalFigure!'




class Triangle(GeometricalFigure):

    def get_triangle_area(self):
        area = self.get_area()
        return area

class Rectangle(GeometricalFigure):

    def get_rectangle_area(self):
        area = self.get_area()
        return area

class Quadrate(GeometricalFigure):

    def get_quadrate_area(self):
        area = self.get_area()
        return area

class Circle(GeometricalFigure):

    def get_circle_area(self):
        area = self.get_area()
        return area


class FakeClass:
    pass



