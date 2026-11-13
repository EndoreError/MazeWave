import random

from src.maze_generator import MazeGenerator
from src.visualizer import Visualizer
from src.pathfinder import Pathfinder

if __name__ == "__main__":  # Выполняется только если на прямую запускать именно эту программу
    width = 0
    height = 0
    seed = 0
    while 3 > width or 100 < width or 3 > height or 100 < height:
        width, height, seed = tuple(map(int, input("width [пробел] height [пробел] seed(0 для случайного): ").split(" ")))
        if seed == 0:
            seed = random.randint(0, 999999999)

    gen = MazeGenerator(width, height, seed)

    wall_maze, terrain_maze, start_point, finish_point = gen.generate_maze_dfs()

    if input("0 - генерация ландшафта: ") == "0":
        terrain_maze = gen.generate_terrain()

    if input("0 - генерация циклов: ") == "0":
        gen.add_cycles(wall_maze)

    l_start = ((start_point[0] - 1) // 2, (start_point[1] - 1) // 2)
    l_finish = ((finish_point[0] - 1) // 2, (finish_point[1] - 1) // 2)

    path = Pathfinder(terrain_maze, wall_maze).find_path(l_start, l_finish)

    if path:
        cells_count = len(path)
        total_cost = sum(terrain_maze.cell_at(cell).cost for cell in path[1:])
        print(f"Путь найден! Длина: {cells_count} клеток. Итоговая стоимость: {total_cost:.2f}")
    else:
        print("Путь не найден!")

    Visualizer(wall_maze, terrain_maze, start_point, finish_point).render(path=path)

    print(start_point, " - start;", finish_point, " - finish;", seed, " - seed")