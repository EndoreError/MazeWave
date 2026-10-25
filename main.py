import random

# from src import pathfinder
from src.maze_generator import MazeGenerator
from src.visualizer import Visualizer

if __name__ == "__main__": # Выполняется только если на прямую запускать именно эту программу
    width = 0
    height = 0
    seed = 0
    while 3 > width or 100 < width or 3 > height or 100 < height:
        width, height, seed = tuple(map(int, input("width [пробел] height [пробел] seed(0 для случайного): ").split(" ")))
        if seed == 0:
            seed = random.randint(0,999999999)
    wall_maze, terrain_maze, start_point, finish_point = MazeGenerator(width, height, seed).generate_maze_dfs()
    if input("0 - генерация ландшафта: ") == "0":
        terrain_maze = MazeGenerator(width, height, seed).generate_terrain()
    Visualizer(wall_maze, terrain_maze, start_point, finish_point).render()
    print(start_point, " - start;", finish_point, " - finish;", seed, " - seed")
    #
    # l_start = (start_point[0] // 2, start_point[1] // 2)
    # l_finish = (finish_point[0] // 2, finish_point[1] // 2)
    # print(pathfinder.Pathfinder(terrain_maze).find_path(l_start, l_finish))