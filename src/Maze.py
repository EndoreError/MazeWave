""" Лабиринт: сетка клеток + старт + финиш """

from src.Cell import Cell
from src.Terrain import WALL

class Maze:
    """Сетка клеток с точками старта и финиша."""

    def __init__(self, width: int, height: int):
        """
        Создаёт пустой лабиринт, полностью заполненный стенами.

        :param width: Ширина в клетках
        :param height: Высота в клетках
        """
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

        # По умолчанию старт в левом верхнем углу, финиш — в правом нижнем.
        # Крайние клетки используем как стены, поэтому +1 и -2.

    def cell_at(self, row: int, col: int) -> Cell:
        """Возвращает клетку по координатам."""
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise IndexError(f"Координаты ({row},{col}) вне лабиринта")
        return self.grid[row][col]

    def set_terrain(self, row: int, col: int, terrain):
        """Меняет тип местности у клетки."""
        self.cell_at(row, col).terrain = terrain

    def neighbors(self, row: int, col: int, step: int):
        """
        Возвращает 4 соседа (без диагоналей) — те, что внутри лабиринта.
        Это генератор, поэтому yield, а не return списка.
        """
        neighborsPoints = []
        for dr, dc in [(-step, 0), (step, 0), (0, -step), (0, step)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.height and 0 <= nc < self.width:
                neighborsPoints.append((nr, nc))
        return neighborsPoints

    def __repr__(self) -> str:
        return f"Maze({self.width}x{self.height})"
