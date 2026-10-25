""" Типы местности и их свойства """

from dataclasses import dataclass
from src.config import terrain_data as data

@dataclass(frozen=True)
class Terrain:
    name: str
    color: tuple[float, float, float]
    cost: float
    passable: bool
    in_print: str = "0"

ROAD = Terrain(data.road_name, data.road_color, data.road_cost, data.road_passible, data.road_in_print)
GRASS = Terrain(data.grass_name, data.grass_color, data.grass_cost, data.grass_passible, data.grass_in_print)
SAND = Terrain(data.sand_name, data.sand_color, data.sand_cost, data.sand_passible, data.sand_in_print)
MOUNTAIN = Terrain(data.mountain_name, data.mountain_color, data.mountain_cost, data.mountain_passible, data.mountain_in_print)
WATER = Terrain(data.water_name, data.water_color, data.water_cost, data.water_passible, data.water_in_print)
WALL = Terrain(data.wall_name, data.wall_color, data.wall_cost, data.wall_passible, data.wall_in_print)

TERRAINS = {}
for t in [ROAD, GRASS, SAND, MOUNTAIN, WATER, WALL]:
    TERRAINS[t.name] = t

def get_terrain(name: str) -> Terrain:
    """ Возвращает объект типа Terrain по имени. Выдаёт ошибку, если Terrain с этим имени нет """
    if name not in TERRAINS:
        raise ValueError(f"Неизвестный тип местности: {name!r}")
    return TERRAINS[name]