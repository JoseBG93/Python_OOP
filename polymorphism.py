
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
    
    def draw(self):
        print(f"Drawing a circle at position ({self.x}, {self.y}) with radius {self.radius}")


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
    
    def draw(self):
        print(f"Drawing a rectangle at position ({self.x}, {self.y}) with height {self.height} and width {self.width}")


class Triangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
    
    def draw(self):
        print(f"Drawing a triangle at position ({self.x}, {self.y}) with height {self.height} and width {self.width}")


# Example usage
def draw_all_shapes(shapes):
    for shape in shapes:
        shape.draw()  # This works because we know all shapes have a draw method

# Create some shapes
circle = Circle(10, 20, 5)
rectangle = Rectangle(30, 40, 15, 25)
triangle = Triangle(50, 60, 20, 30)


# Put them in a list and draw them all
shapes = [circle, rectangle, triangle]
draw_all_shapes(shapes)
        