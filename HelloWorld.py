from src.Terrain import *
from src.Cell import *

print("Hello World")
print(get_terrain('water').cost)
a = Cell(5, 7, WATER)
b = Cell(6, 1)
print(a.cost, a, b)