from abc import ABC, abstractmethod
import math

class Shape(ABC):
    #this gives the shapes to have an area property
    @abstractmethod
    def area(self):
        pass
 
class Three_D_Shape(ABC):
       #new set of rules to originate
       @abstractmethod
       def volume(self):
           pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        #overides the abstract method with actual math
        return math.pi * (self.radius **2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height * 0.5
    
class Box(Three_D_Shape):
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        
    def volume(self):
        return self.width * self.height * self.depth