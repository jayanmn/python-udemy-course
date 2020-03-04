class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        area = self.pi * (self.radius ** 2)
        return self.height * area

    def surface_area(self):
        area_circumference = 2 * self.pi * self.radius * self.height
        area_bottom = self.pi * (self.radius ** 2)
        return (2 * area_bottom) + area_circumference
        pass


class Line:
    '''
     coord1 : tuple representing x, y coordinate of one end
     coord2 : tuple representing x, y coordinate of another end
    '''

    def __init__(self, coord1, coord2):
        self.x1, self.y1 = coord1
        self.x2, self.y2 = coord2

    def distance(self):
        '''
            distance = sqrt((x2-x1)^2 + (y2-y1)^2)
        '''
        x_distance = self.x2 - self.x1
        y_distance = self.y2 - self.y1
        return (x_distance ** 2 + y_distance ** 2) ** 0.5  # square root
        pass

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)
        pass


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)
assert line.distance() == 9.433981132056603
assert line.slope() == 1.6

# EXAMPLE OUTPUT
c = Cylinder(2, 3)
assert c.surface_area() == 94.2
assert c.volume() == 56.52
