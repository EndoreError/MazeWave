from src.Terrain import *
from src.Maze import *

print("Hello World")
print(get_terrain('water').cost)
a = Cell(5, 7, WATER)
b = Cell(6, 1)
print(a.cost, a, b)
m=Maze(5, 5)
m.cell_at(1,1).terrain = ROAD
m.cell_at(2,1).terrain = ROAD
m.cell_at(3,1).terrain = ROAD
m.cell_at(1,2).terrain = ROAD
m.cell_at(1,3).terrain = ROAD
m.cell_at(2,3).terrain = ROAD
m.cell_at(3,3).terrain = ROAD
for i in range(5):
    for j in range(5):
        print(m.cell_at(i,j).terrain.name, end=" ")
    print()
for i,j in m.neighbors(1,3):
    print(m.cell_at(i,j).terrain.name, end=" ")