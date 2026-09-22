""" Лабиринт: сетка клеток + старт + финиш """

from src.cell import Cell
from src.terrain import WALL

class Maze:
    """ Сетка клеток с точками старта и финиша """

    def __init__(self, width: int, height: int):
        """ Создаёт пустой лабиринт, полностью заполненный стенами """
        if width < 3 or height < 3:
            raise ValueError("Размер лабиринта должен быть не меньше 3x3")

        self.width = width
        self.height = height
        self.grid = []
        for r in range(height):
            row = []
            for c in range(width):
                row.append(Cell(r, c, WALL))
            self.grid.append(row)

    def cell_at(self, point: tuple[int, int]) -> Cell:
        """ Возвращает клетку по координатам """
        if not (0 <= point[0] < self.height and 0 <= point[1] < self.width):
            raise IndexError(f"Координаты ({point[0]},{point[1]}) вне лабиринта")
        return self.grid[point[0]][point[1]]

    def set_terrain(self, point: tuple[int, int], terrain):
        """ Меняет тип местности у клетки """
        self.cell_at(point).terrain = terrain

    def neighbors(self, row: int, col: int, step: int):
        """
        Возвращает 4 соседа (без диагоналей) — те, что внутри лабиринта.
        Это генератор, поэтому yield, а не return списка.
        """
        neighbors_points = []
        for dr, dc in [(-step, 0), (step, 0), (0, -step), (0, step)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.height and 0 <= nc < self.width:
                neighbors_points.append((nr, nc))
        return neighbors_points

    def __repr__(self) -> str:
        return f"Maze({self.width}x{self.height})"