import random
from random import seed

from src.maze_generator import MazeGenerator
from src.visualizer import Visualizer

if __name__ == "__main__": # Выполняется только если на прямую запускать именно эту программу
    width = 0
    height = 0
    seed = 0
    while 3 > width or 100 < width or 3 > height or 100 < height:
        width, height, seed = tuple(map(int, input("width [пробел] height [пробел] seed(0 для случайного): ").split(" ")))
        if seed == 0:
            seed = random.randint(0,99999999)
    wall_maze, terrain_maze, start_point, finish_point = MazeGenerator(width, height, seed).generate_maze_dfs()
    if input("0 - генерация ландшафта: ") == "0":
        terrain_maze = MazeGenerator(width, height, seed).generate_terrain()
    Visualizer(wall_maze, terrain_maze, start_point, finish_point).render()
    print(start_point, " - start;", finish_point, " - finish;", seed, " - seed")

# Визуализация территории в консоли
#     for i in range(terrain.height):
#         for j in range(terrain.width):
#             if (i, j) == start_point: print("s", end=" ")
#             elif (i, j) == finish_point: print("f", end=" ")
#             else: print(terrain.cell_at((i, j)).terrain.in_print, end=" ")
#         print()

# Визуализация стен в консоли
#     for i in range(wall_maze.height):
#         for j in range(wall_maze.width):
#             if (i, j) == start_point: print("s", end=" ")
#             elif (i, j) == finish_point: print("f", end=" ")
#             else: print(wall_maze.cell_at((i, j)).terrain.in_print, end=" ")
#         print()