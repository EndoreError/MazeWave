""" Поиск пути алгоритмом Дейкстра """

from src.maze import Maze
from src.terrain import WALL

class Pathfinder:
    """ Ищет путь минимальной стоимости по логической сетке """

    def __init__(self, terrain_maze: Maze, wall_maze: Maze):
        self.terrain_maze = terrain_maze
        self.wall_maze = wall_maze

    def _has_passage(self, cell1: tuple[int, int], cell2: tuple[int, int]) -> bool:
        """ Проверяет, есть ли проход между двумя соседними логическими клетками """
        wall_row = cell1[0] + cell2[0] + 1
        wall_col = cell1[1] + cell2[1] + 1

        return self.wall_maze.cell_at((wall_row, wall_col)).terrain != WALL

    def find_path(self, start: tuple[int, int], finish: tuple[int, int]) -> list[tuple[int, int]]:
        """ Основной метод поиска пути """
        if start == finish:
            return [start]

        dist = {start: 0.0}
        came_from = {}
        visited = set()
        queue = [(0.0, start)]

        # Основной алгоритм
        while queue:
            min_index = 0
            for i in range(1, len(queue)):
                if queue[i][0] < queue[min_index][0]:
                    min_index = i

            current_dist, current_cell = queue.pop(min_index)

            if current_cell in visited:
                continue

            if current_cell == finish:
                break

            visited.add(current_cell)

            for neighbor in self.terrain_maze.neighbors(current_cell, 1):
                if neighbor in visited:
                    continue

                if not self._has_passage(current_cell, neighbor):
                    continue

                neighbor_cost = self.terrain_maze.cell_at(neighbor).cost
                new_dist = current_dist + neighbor_cost

                if new_dist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = new_dist
                    came_from[neighbor] = current_cell
                    queue.append((new_dist, neighbor))

        if finish not in dist:
            return []

        path = []
        current = finish
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)

        path.reverse()

        return path
