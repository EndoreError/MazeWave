from src.maze_generator import MazeGenerator
from src.terrain import WATER, GRASS
from src.visualizer import Visualizer

if __name__ == "__main__":
    wall_maze, terrain_maze, start_point, finish_point = MazeGenerator(30, 30, 10293).generate_dfs()
    terrain_maze.set_terrain((0, 1), WATER)
    terrain_maze.set_terrain((2, 1), GRASS)
    terrain_maze.set_terrain((5, 2), GRASS)
    terrain_maze.set_terrain((6, 2), GRASS)
    terrain_maze.set_terrain((12, 5), GRASS)
    terrain_maze.set_terrain((12, 1), GRASS)
    terrain_maze.set_terrain((22, 21), GRASS)
    Visualizer(wall_maze, terrain_maze, start_point, finish_point).terrain_render()