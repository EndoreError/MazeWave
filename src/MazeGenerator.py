""" Генератор лабиринта """

import random

from src.Maze import Maze
from src.Terrain import ROAD, WALL

class MazeGenerator:
    """Генерация лабиринта по seed."""

    def __init__(self, width: int, height: int, seed: int):
        """
        :param width: ширина лабиринта
        :param height: высота лабиринта
        :param seed: зерно случайности (для воспроизводимости)
        """
        self.width = width
        self.height = height
        self.seed = seed

        # Собственный генератор случайности — не глобальный.
        # Это ключ к воспроизводимости: один seed → одна карта всегда.
        self.rng = random.Random(seed)
        self.start: tuple[int, int] = (self.rng.randint(0, self.width - 1), self.rng.randint(0, self.height - 1))
        self.finish: tuple[int, int]

    def generatedfs(self) -> Maze:
        """ Из объекта Maze генерирует другой объект Maze, заполненный лабиринтом """
        maze = Maze(self.width, self.height)
        mazeBarrier = Maze(self.width * 2 + 1, self.height * 2 + 1)

        stack = [self.start]
        visited = set()
        visited.add(self.start)
        maze.set_terrain(self.start[0], self.start[1], ROAD)
        mazeBarrier.set_terrain(self.start[0] * 2 + 1, self.start[1] * 2 + 1, ROAD)

        while stack:

            neighbours = []
            for i in maze.neighbors(stack[-1][0], stack[-1][1], 1):
                if i not in visited:
                    neighbours.append(i)

            if neighbours:
                nowNeighbour = self.rng.choice(neighbours)
                visited.add(nowNeighbour)
                maze.set_terrain(nowNeighbour[0], nowNeighbour[1], ROAD)
                mazeBarrier.set_terrain(nowNeighbour[0] * 2 + 1, nowNeighbour[1] * 2 + 1, ROAD)
                wallPoint = (nowNeighbour[0] + stack[-1][0] + 1, nowNeighbour[1] + stack[-1][1] + 1)
                mazeBarrier.set_terrain(wallPoint[0], wallPoint[1], ROAD)
                stack.append(nowNeighbour)
            else: stack.pop()

        return mazeBarrier