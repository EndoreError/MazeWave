""" Одна клетка лабиринта """

from dataclasses import dataclass

from src.Terrain import Terrain, WALL


@dataclass
class Cell:
    """ Клетка сетки """
    row: int
    col: int
    terrain: Terrain = WALL

    #property Чтобы не писать () при вызове метода, берёт значение из self
    @property
    def is_wall(self) -> bool:
        """ True, если клетка непроходима """
        return not self.terrain.passable

    @property
    def cost(self) -> float:
        """ Стоимость прохода через эту клетку """
        return self.terrain.cost

    def __repr__(self) -> str:
        """ Как клетка показывается в консоли """
        return f"Клетка (Строка: {self.row}, Столбец: {self.col}, Тип: {self.terrain.name})"