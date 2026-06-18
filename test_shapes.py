import pytest
from shapes import Rectangle
from shapes import Triangle
from shapes import Circle
from shapes import Box
import math

# @pytest.fixture
# def my_rectangle():
#     return Rectangle(width=10, height=5)

# def test_area(my_rectangle):
#     assert my_rectangle.area() == 50
    



# def area_of_triangle():
#     width = float(input("width?"))
#     height = float(input("height?"))
#     return Triangle(width, height)

# def main():
#     my_triangle = area_of_triangle()
    
#     my_triangle_2 = area_of_triangle()
    
#     print(my_triangle.area())
    
#     print(my_triangle_2.area())
    
    
# main()
    
# @pytest.fixture
# def area_of_circle():
#     return Circle(3)

# def test_circles(area_of_circle):
#     assert area_of_circle.area() == 9 * math.pi    
    
def volume_box():
    width = float(input("width?"))
    height = float(input("height?"))
    depth= float(input("depth?"))
    return Box(width, height, depth)
    
    
def main():
    my_box = volume_box()
    print(my_box.volume())
    
main()