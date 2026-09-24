""" Типы местности и их свойства """

from dataclasses import dataclass

@dataclass(frozen=True)
class Terrain:
    name: str
    color: tuple[float, float, float]
    cost: float
    passable: bool = True

ROAD = Terrain("road", (200/255.0, 200/255.0, 200/255.0), 1.0)
GRASS = Terrain("grass", (170/255.0, 250/255.0, 170/255.0), 1.5)
SAND = Terrain("sand", (245/255.0, 230/255.0, 165/255.0), 2.0)
TRAP = Terrain("trap", (75/255.0, 75/255.0, 75/255.0), 5.0)
WATER = Terrain("water", (65/255.0, 130/255.0, 240/255.0), 10.0)
WALL = Terrain("wall", (0/255.0, 0/255.0, 0/255.0), float("inf"), passable=False)

TERRAINS = {}
for t in [ROAD, GRASS, SAND, TRAP, WATER, WALL]:
    TERRAINS[t.name] = t

def get_terrain(name: str) -> Terrain:
    """ Возвращает объект типа Terrain по имени. Выдаёт ошибку, если Terrain с этим имени нет """
    if name not in TERRAINS:
        raise ValueError(f"Неизвестный тип местности: {name!r}")
    return TERRAINS[name]