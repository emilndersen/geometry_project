# Geometry Project

Python library implementing geometric shapes with area calculation and unit tests.

## Features

- **Circle**: calculate area
- **Triangle**: calculate area, check if right-angled
- Polymorphic area calculation for any shape
- Easy to extend with new shapes
- Unit tests included

## Usage

```python
from geometry_lib import Circle, Triangle

c = Circle(5)
print(c.area())  # Output: 78.53981633974483

t = Triangle(3, 4, 5)
print(t.area())       # Output: 6.0
print(t.is_right())   # Output: True
