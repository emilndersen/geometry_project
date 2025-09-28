import math
import unittest
from geometry_lib import Circle, Triangle

# Тут пишу тесты для всех фигур
class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        # Проверяю, правильно ли считается площадь круга
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        # Проверяю площадь треугольника
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_right_triangle(self):
        # Проверяю, что треугольник прямоугольный
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_not_right_triangle(self):
        # Проверяю, что треугольник НЕ прямоугольный
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())

    def test_polymorphic_area_calculation(self):
        # Проверяю, что можно вызвать area() для любой фигуры
        shapes = [Circle(1), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]  # вызываю area() для каждой фигуры
        self.assertAlmostEqual(areas[0], math.pi)
        self.assertAlmostEqual(areas[1], 6)

if __name__ == "__main__":
    unittest.main()
