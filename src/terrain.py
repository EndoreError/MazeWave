""" Типы местности и их свойства """

from dataclasses import dataclass

@dataclass(frozen=True)
class Terrain:
    name: str
    color: tuple[float, float, float]
    cost: float
    in_print: str = "0"

ROAD = Terrain("road", (250/255.0, 250/255.0, 250/255.0), 1.0, ".")
GRASS = Terrain("grass", (200/255.0, 250/255.0, 200/255.0), 1.5, "g")
SAND = Terrain("sand", (245/255.0, 230/255.0, 165/255.0), 2.0, "s")
TRAP = Terrain("trap", (200/255.0, 200/255.0, 200/255.0), 5.0, "t")
WATER = Terrain("water", (150/255.0, 200/255.0, 240/255.0), 10.0, "w")
WALL = Terrain("wall", (0/255.0, 0/255.0, 0/255.0), float("inf"), "#")

TERRAINS = {}
for t in [ROAD, GRASS, SAND, TRAP, WATER, WALL]:
    TERRAINS[t.name] = t

def get_terrain(name: str) -> Terrain:
    """ Возвращает объект типа Terrain по имени. Выдаёт ошибку, если Terrain с этим имени нет """
    if name not in TERRAINS:
        raise ValueError(f"Неизвестный тип местности: {name!r}")
    return TERRAINS[name]