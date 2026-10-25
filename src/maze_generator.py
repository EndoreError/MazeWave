""" Генератор лабиринта """

import random

from src.terrain import *
from src.maze import Maze
from src.config import generator_data

class MazeGenerator:
    """ Генерация лабиринта по seed """

    def __init__(self, width: int, height: int, seed: int):

        self.width = width
        self.height = height
        self.seed = seed

        self.rng = random.Random(seed)
        self.start: tuple[int, int] = (self.rng.randint(0, self.height - 1), self.rng.randint(0, self.width - 1))
        self.finish: tuple[int, int] = self.start

    def generate_maze_dfs(self) -> tuple[Maze, Maze, tuple[int, int], tuple[int, int]]:
        """
        Из объекта Maze генерирует другой объект Maze, заполненный лабиринтом,
        выдаёт кортеж с лабиринтом точкой старта и финиша
        """
        terrain_maze = Maze(self.width, self.height)
        wall_maze = Maze(self.width * 2 + 1, self.height * 2 + 1)

        stack = [self.start]
        visited = {self.start}
        terrain_maze.set_terrain(self.start, ROAD)
        wall_maze.set_terrain((self.start[0] * 2 + 1, self.start[1] * 2 + 1), ROAD)

        while stack:

            neighbours = []
            for i in terrain_maze.neighbors(stack[-1], 1):
                if i not in visited:
                    neighbours.append(i)

            if neighbours:
                now_neighbour = self.rng.choice(neighbours)
                visited.add(now_neighbour)
                terrain_maze.set_terrain(now_neighbour, ROAD)
                wall_maze.set_terrain((now_neighbour[0] * 2 + 1, now_neighbour[1] * 2 + 1), ROAD)
                wall_point = (now_neighbour[0] + stack[-1][0] + 1, now_neighbour[1] + stack[-1][1] + 1)
                wall_maze.set_terrain(wall_point, ROAD)
                stack.append(now_neighbour)
            else: stack.pop()

        finish_stack = []

        for row in range(wall_maze.height):
            for col in range(wall_maze.width):
                cell = wall_maze.cell_at((row, col))
                if cell.terrain != WALL:
                    n = 0
                    for i in wall_maze.neighbors((row, col), 1):
                        if wall_maze.cell_at(i).terrain == WALL: n+=1
                    if n == 3: finish_stack.append((row, col))

        physical_start = (self.start[0] * 2 + 1, self.start[1] * 2 + 1)
        physical_finish = self.rng.choice(finish_stack)

        n = 0
        while abs(physical_start[0] - physical_finish[0]) <= wall_maze.height // 2 - 1 or abs(physical_start[1] - physical_finish[1]) <= wall_maze.width // 2 - 1:
            physical_finish = self.rng.choice(finish_stack)
            if n > wall_maze.width + wall_maze.height:
                break
            n += 1

        return wall_maze, terrain_maze, physical_start, physical_finish

    def generate_terrain(self) -> Maze:
        """
        Из объекта Maze генерирует другой объект Maze, заполненный ландшафтом,
        выдаёт только лабиринт с ландшафтом
        """
        terrain_maze = Maze(self.width, self.height)

        for row in range(terrain_maze.height):
            for col in range(terrain_maze.width):
                terrain_maze.cell_at((row, col)).height = self.rng.random()
                terrain_maze.cell_at((row, col)).wet = self.rng.random()

        # Сглаживание высоты и влажности
        self._smooth_field(terrain_maze, "height", generator_data.smooth_field_height_passes)
        self._smooth_field(terrain_maze, "wet", generator_data.smooth_field_wet_passes)

        for row in range(terrain_maze.height):
            for col in range(terrain_maze.width):
                wet = terrain_maze.cell_at((row, col)).wet
                height = terrain_maze.cell_at((row, col)).height

                if wet > 0.70:
                    terrain_maze.set_terrain((row, col), WATER)

                elif height > 0.75 and wet < 0.50:
                    terrain_maze.set_terrain((row, col), MOUNTAIN)

                elif height > 0.65 and wet < 0.30:
                    terrain_maze.set_terrain((row, col), MOUNTAIN)

                elif wet > 0.60:
                    terrain_maze.set_terrain((row, col), SAND)

                elif wet < 0.30:
                    terrain_maze.set_terrain((row, col), SAND)

                elif height < 0.25 and wet > 0.60:
                    terrain_maze.set_terrain((row, col), WATER)

                else:
                    terrain_maze.set_terrain((row, col), GRASS)

        return terrain_maze

    @staticmethod
    def _smooth_field(maze: Maze, field: str, passes: int):
        """ Сглаживание поля (height или wet) с нормализацией после каждого прохода. """
        for _ in range(passes):
            min_v, max_v = 1.0, 0.0
            for row in range(maze.height):
                for col in range(maze.width):
                    av = 0
                    neighbours_points = (maze.neighbors((row, col), 1) + maze.x_neighbors((row, col), 1))

                    for i in neighbours_points:
                        av += getattr(maze.cell_at(i), field)
                    av /= len(neighbours_points)

                    if min_v > av: min_v = av
                    if max_v < av: max_v = av

                    setattr(maze.cell_at((row, col)), field, av)

            for row in range(maze.height):
                for col in range(maze.width):
                    cell = maze.cell_at((row, col))

                    setattr(cell, field,(getattr(cell, field) - min_v) / (max_v - min_v))