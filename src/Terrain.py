""" Типы местности и их свойства """

from dataclasses import dataclass


@dataclass(frozen=True)
class Terrain:
    name: str
    color: tuple[int, int, int]
    cost: float
    passable: bool = True

ROAD = Terrain("road", (255, 255, 255), 1.0)
GRASS = Terrain("grass", (170, 250, 170), 1.5)
SAND = Terrain("sand", (245, 230, 165), 2.0)
TRAP = Terrain("trap", (75, 75, 75), 5.0)
WATER = Terrain("water", (65, 130, 240), 10.0)
WALL = Terrain("wall", (0, 0, 0), float("inf"), passable=False)

TERRAINS = {}
for t in [ROAD, GRASS, SAND, TRAP, WATER, WALL]:
    TERRAINS[t.name] = t

def get_terrain(name: str) -> Terrain:
    """Возвращает объект типа Terrain по имени. Выдаёт ошибку, если Terrain с этим имени нет."""
    if name not in TERRAINS:
        raise ValueError(f"Неизвестный тип местности: {name!r}")
    return TERRAINS[name]