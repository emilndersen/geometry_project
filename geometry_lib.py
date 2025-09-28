import math

# Это базовый класс для всех фигур
class Shape:
    def area(self):
        # Тут просто заготовка: у каждой фигуры должен быть свой способ вычисления площади
        raise NotImplementedError("Метод area должен быть реализован в наследнике")


# Класс круга
class Circle(Shape):
    def __init__(self, radius):
        # Просто храним радиус круга
        self.radius = radius

    def area(self):
        # Вычисляем площадь круга по формуле π * r^2
        return math.pi * self.radius ** 2


# Класс треугольника
class Triangle(Shape):
    def __init__(self, a, b, c):
        # Сохраняем стороны треугольника
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Формула Герона для площади треугольника
        s = (self.a + self.b + self.c) / 2  # полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        # Проверяем, прямоугольный ли треугольник
        sides = sorted([self.a, self.b, self.c])
        # Теорема Пифагора: a^2 + b^2 примерно равно c^2
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)