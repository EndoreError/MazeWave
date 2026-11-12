from dataclasses import dataclass

@dataclass
class TerrainData:
    road_name: str = "road"
    road_color: tuple[float, float, float] = (250/255.0, 250/255.0, 250/255.0)
    road_cost: float = 1.0
    road_passible: bool = True
    road_in_print: str = " "

    grass_name: str = "grass"
    grass_color: tuple[float, float, float] = (200/255.0, 250/255.0, 200/255.0)
    grass_cost: float = 1.5
    grass_passible: bool = True
    grass_in_print: str = "g"

    sand_name: str = "sand"
    sand_color: tuple[float, float, float] = (245/255.0, 230/255.0, 165/255.0)
    sand_cost: float = 2.0
    sand_passible: bool = True
    sand_in_print: str = "s"

    mountain_name: str = "mountain"
    mountain_color: tuple[float, float, float] = (200/255.0, 200/255.0, 200/255.0)
    mountain_cost: float = 5.0
    mountain_passible: bool = True
    mountain_in_print: str = "t"

    water_name: str = "water"
    water_color: tuple[float, float, float] = (150/255.0, 200/255.0, 240/255.0)
    water_cost: float = 10.0
    water_passible: bool = True
    water_in_print: str = "w"

    wall_name: str = "wall"
    wall_color: tuple[float, float, float] = (0/255.0, 0/255.0, 0/255.0)
    wall_cost: float = float("inf")
    wall_passible: bool = False
    wall_in_print: str = "#"

@dataclass
class GeneratorData:
    smooth_field_height_passes: int = 8
    smooth_field_wet_passes: int = 6

    max_maze_size: int = 100
    min_maze_size: int = 3

@dataclass
class VisualizerData:
    tile_size: int = 1
    wall_linewidth: int = 6
    start_color: tuple[str, str, str] = ('#10ff10', '#ffffff', '#000000')
    finish_color: tuple[str, str, str] = ('#ff0000', '#ffffff', '#000000')
    marker_size: int = 30

terrain_data = TerrainData
generator_data = GeneratorData
visualizer_data = VisualizerData