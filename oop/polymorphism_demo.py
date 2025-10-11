# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method for calculating area — must be overridden by subclasses"""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width"""
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle"""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate area of a circle"""
        return math.pi * (self.radius ** 2)
