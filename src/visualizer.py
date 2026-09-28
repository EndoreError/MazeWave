""" Визуализация лабиринта: тонкие стены, крупные цветные клетки """

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

from src.maze import Maze
from src.terrain import *


class Visualizer:
    def __init__(self,wall_maze: Maze, terrain_maze: Maze, start_point, finish_point):
        self.wall_maze = wall_maze
        self.terrain_maze = terrain_maze
        self.start_point = start_point
        self.finish_point = finish_point

        self.tile_size = 1
        self.wall_linewidth = 4

    def terrain_array_generator(self):
        terrain_array = []
        for y in range(self.terrain_maze.height):
            row = []
            for x in range(self.terrain_maze.width):
                row.append(self.terrain_maze.cell_at((y,x)).terrain.color)
            terrain_array.append(row)
        return  np.array(terrain_array)

    def wall_array_generator(self):
        wall_array = []
        for y in range(self.wall_maze.height):
            for x in range(self.wall_maze.width):
                if self.wall_maze.cell_at((y, x)).terrain != WALL:
                    continue
                if x + 1 < self.wall_maze.width and self.wall_maze.cell_at((y, x + 1)).terrain == WALL:
                    wall_array.append([(x, y), (x + 1, y,)])
                if y + 1 < self.wall_maze.height and self.wall_maze.cell_at((y + 1, x)).terrain == WALL:
                    wall_array.append([(x, y), (x, y + 1)])
        return wall_array


    def render(self):
        fig, ax = plt.subplots(figsize=(self.terrain_maze.width * self.tile_size, self.terrain_maze.height * self.tile_size))

        sr, sc = (self.start_point[0] - 1) // 2, (self.start_point[1] - 1) // 2
        ax.plot(2 * sc + 1, 2 * sr + 1, 'o', color='#10ff10', markersize=30, zorder=3)
        fr, fc = (self.finish_point[0] - 1) // 2, (self.finish_point[1] - 1) // 2
        ax.plot(2 * fc + 1, 2 * fr + 1, 'o', color='#ff0000', markersize=30, zorder=3)
        ax.imshow(self.terrain_array_generator(), extent=(0, 2 * self.terrain_maze.width, 2 * self.terrain_maze.height, 0), zorder=1)
        ax.add_collection(LineCollection(self.wall_array_generator(), colors=WALL.color, linewidths=self.wall_linewidth, zorder=2))

        ax.axis('off')
        plt.tight_layout()
        plt.show()