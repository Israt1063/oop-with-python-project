from math import pi
class Shape:
    def __init__(self,name) :
        self.name=name

class Rectangle(Shape):
    def __init__(self, name,length,width):
        self.length = length
        self.width = width
        super().__init__(name)
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name,radious):
        self.radious = radious
        super().__init__(name)

    def area(self):
        return pi * self.radious *self.radious
    
math = Rectangle('book',4,3)
print(math.area())

math2 = Circle('book2',4)
print(math2.area())