import math
import unittest
from geometry_lib import Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())

    def test_polymorphic_area_calculation(self):
        shapes = [Circle(1), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]  # вместо calculate_area
        self.assertAlmostEqual(areas[0], math.pi)
        self.assertAlmostEqual(areas[1], 6)
