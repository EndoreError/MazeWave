# """ Поиск пути """
#
# from src.maze import Maze
#
#
# class Pathfinder:
#     """ Ищет путь минимальной стоимости """
#
#     def __init__(self, terrain_maze: Maze, wall_maze: Maze):
#         self.terrain_maze = terrain_maze
#         self.wall_maze = wall_maze
#
#     def find_path_dijkstra(self, start: tuple[int, int], finish: tuple[int, int]) -> list[tuple[int, int]]:
#         """ Алгоритм поиска пути Дейкстра """
#         path = {start: start}
#         while finish not in path:
