import math
"""This program uses object-oriented program to
calculate different types of shape area's like circles,
squares, rectangles and triangles.
This program uses polymorhism to achieve this. """


class ShapeArea(object): #superclass for all shapes
    """docstring for ShapeArea."""
    def __init__(self, shapeName, numSides): #constructor
        self.shapeName = shapeName
        self.numSides = numSides

    def __repr__(self):
        retrun ("%s: with %d sides") %(self.shapeName, self.numSides)

class Rectangle(ShapeArea): #rectangle shape class subclass of ShapeArea
    """docstring for Rectangle."""
    def __init__(self, shapeName, numSides, length, width):
        super(Rectangle,self).__init__(shapeName, numSides)
        self.length = length
        self.width = width

    def calcArea(self): #calculates area pf a rectangle
        return (self.width * self.length)

    def __repr__(self):  #toString: overrides superclass tostring
        return ("%s has %d sides (length: %d width: %d)") \
            % (self.shapeName, self.numSides, self.length, self.width)

class Square(ShapeArea): #square shape subclass of ShapeArea
    """docstring for Square."""
    def __init__(self, shapeName, numSides, length):
        super(Square, self).__init__(shapeName, numSides)
        self.length = length

    def calcArea(self): #calculates area of a square
        return (self.length **2)

    def __repr__(self):  #toString: overrides superclass tostring
        return ("%s has sides: %d (length: %d)") \
            % (self.shapeName, self.numSides, self.length)

class Triangle(ShapeArea):  #triangle shape subclass of ShapeArea
    """docstring for Trianle."""
    def __init__(self, shapeName, numSides, height, base):
        super(Triangle, self).__init__(shapeName, numSides)
        self.height = height
        self.base = base

    def calcArea(self): #calculates the area of a triangle
        return (self.height * self.base * 0.5)

    def __repr__(self): #toString: overrides superclass tostring
        return ("%s has %d sides (height: %d  base: %d)") \
            % (self.shapeName, self.numSides, self.height, self.base)

class Circle(ShapeArea):   #circle shape
    """docstring for Circle."""
    def __init__(self, shapeName, numSides, radius):
        super(Circle, self).__init__(shapeName, numSides)
        self.radius = radius

    def calcArea(self):  #calculates area of a circle
        return (self.radius**2) *math.pi

    def __repr__(self):  #toString: overrides superclass tostring
        return ("%s has %d sides (radius: %d)") \
            % (self.shapeName, self.numSides, self.radius)

rec = Rectangle("Rectangle", 4 , 5, 3)
print ("*****Welcome to Area Calculator (%s)*****" %(rec.shapeName))
print ("Created shape: ",rec.shapeName)
print (rec)
print ("Area: ", str(rec.calcArea()))
print ("\n")
sqr = Square("Square", 4 , 5)
print ("*****Welcome to Area Calculator (%s)*****" %(sqr.shapeName))
print ("Created shape: ",sqr.shapeName)
print (sqr)
print ("Area: ", str(sqr.calcArea()))
print ("\n")
tri = Triangle("Triangle", 3 , 3,2)
print ("*****Welcome to Area Calculator (%s)*****" %(tri.shapeName))
print ("Created shape: ",tri.shapeName)
print (tri)
print ("Area: ", str(tri.calcArea()))
print ("\n")
cir = Circle("Circle", 0, 7)
print ("*****Welcome to Area Calculator (%s)*****" %(cir.shapeName))
print ("Created shape: ",cir.shapeName)
print (tri)
print ("Area: %0.2f" % (cir.calcArea()))
