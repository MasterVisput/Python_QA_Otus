
class GeometricalFigure:

    def __init__(self, name=None, area=None, angles=None, perimeter=None):
        self.name = name
        self.area = area
        self.angles = angles
        self.perimeter = perimeter


    def get_name(self):
        return self.name


    def get_area(self):
        return self.area


    def get_angles(self):
        return self.angles


    def get_perimeter(self):
        return self.perimeter




rectangke = GeometricalFigure()
rectangke.name = 'rect'
print(rectangke.get_name())

