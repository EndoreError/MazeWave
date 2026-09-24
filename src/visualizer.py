""" Визуализация лабиринта: тонкие стены, крупные цветные клетки """

import matplotlib.pyplot as plt
import numpy as np

from src.maze import Maze


class Visualizer:
    """ Рисует лабиринт """

    def __init__(self,wall_maze: Maze, terrain_maze: Maze, start_point, finish_point):
        self.wall_maze = wall_maze
        self.terrain_maze = terrain_maze
        self.start_point = start_point
        self.finish_point = finish_point

        self.tile_size = 30
        self.wall_size = 6

    def terrain_array_generator(self):
        terrain_array = []
        for y in range(self.terrain_maze.height):
            row = []
            for x in range(self.terrain_maze.width):
                row.append(self.terrain_maze.cell_at((y,x)).terrain.color)
            terrain_array.append(row)
        return  np.array(terrain_array)


    def terrain_render(self):
        plt.figure(figsize=(self.tile_size, self.tile_size))
        plt.imshow(self.terrain_array_generator(), origin='upper')
        plt.axis('off')
        plt.show()