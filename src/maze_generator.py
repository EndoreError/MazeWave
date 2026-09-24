""" Генератор лабиринта """

import random

from src.maze import Maze
from src.terrain import ROAD

class MazeGenerator:
    """ Генерация лабиринта по seed """

    def __init__(self, width: int, height: int, seed: int):

        self.width = width
        self.height = height
        self.seed = seed

        self.rng = random.Random(seed)
        self.start: tuple[int, int] = (self.rng.randint(0, self.height - 1), self.rng.randint(0, self.width - 1))
        self.finish: tuple[int, int] = self.start

    def generate_dfs(self) -> tuple[Maze, Maze, tuple[int, int], tuple[int, int]]:
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
            else:
                if self.finish == self.start:
                    self.finish = stack[-1]
                stack.pop()

        physical_start = (self.start[0] * 2 + 1, self.start[1] * 2 + 1)
        physical_finish = (self.finish[0] * 2 + 1, self.finish[1] * 2 + 1)

        return wall_maze, terrain_maze, physical_start, physical_finish