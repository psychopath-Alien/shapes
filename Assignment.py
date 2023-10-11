class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print('Circle Properties')
        print(f'Radius:     {self.radius} meters')
        print(f'Area:       {self.area()} meters squared') 
        print(f'Perimeter:  {self.perimeter()} meters')

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side*self.side
    
    def perimeter(self):
        return self.side*4
    
    def display(self):
        print('Square Properties')
        print(f'Side:       {self.side} meters')
        print(f'Area:       {self.area()} meters squared') 
        print(f'Perimeter:  {self.perimeter()} meters')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (self.width*2)+(self.height*2)
    
    def display(self):
        print('Rectangle Properties')
        print(f'Width:      {self.width} meters')
        print(f'Height:     {self.height} meters')
        print(f'Area:       {self.area()} meters squared') 
        print(f'Perimeter:  {self.perimeter()} meters')

class Triangle:
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.base*self.height
    
    def perimeter(self):
        return self.base+self.side1+self.side2
    
    def display(self):
        print('Triangle Properties')
        print(f'Side 1:     {self.side1} meters')
        print(f'Side 2:     {self.side2} meters')
        print(f'Base:       {self.base} meters')
        print(f'Height:     {self.height} meters')
        print(f'Area:       {self.area()} meters squared') 
        print(f'Perimeter:  {self.perimeter()} meters')

circle = Circle(5)
circle.display()
print()
square = Square(5)
square.display()
print()
rectangle = Rectangle(5, 6)
rectangle.display()
print()
triangle = Triangle(5, 6, 7, 8)
triangle.display()