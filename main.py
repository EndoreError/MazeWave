import random

from src.maze_generator import MazeGenerator
from src.visualizer import Visualizer
from src.pathfinder import Pathfinder
from src.config import generator_data

if __name__ == "__main__":
    width = 0
    height = 0
    seed = 0

    while True:
        try:
            user_input = input("width [пробел] height [пробел] seed(0 для случайного): ").split()

            if len(user_input) != 3:
                print("Ошибка: нужно ввести ровно 3 числа через пробел.")
                continue

            width, height, seed = map(int, user_input)

            if not (generator_data.min_maze_size <= width <= generator_data.max_maze_size and
                    generator_data.min_maze_size <= height <= generator_data.max_maze_size):
                print(
                    f"Ошибка: размеры должны быть от {generator_data.min_maze_size} до {generator_data.max_maze_size}.")
                continue
            break

        except ValueError:
            print("Ошибка: вводите только целые числа.")

    if seed == 0:
        seed = random.randint(0, 999999999)

    gen = MazeGenerator(width, height, seed)
    wall_maze, terrain_maze, start_point, finish_point = gen.generate_maze_dfs()

    if input("0 - генерация ландшафта (любой другой символ - пропустить): ") == "0":
        terrain_maze = gen.generate_terrain()

    if input("0 - генерация циклов (любой другой символ - пропустить): ") == "0":
        gen.add_cycles(wall_maze, finish_point)

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