from src.maze_generator import MazeGenerator
from src.terrain import WATER, GRASS, TRAP, SAND
from src.visualizer import Visualizer

if __name__ == "__main__": # Выполняется только если на прямую запускать именно эту программу
    wall_maze, terrain_maze, start_point, finish_point = MazeGenerator(6, 7, 42).generate_dfs()
    terrain_maze.set_terrain((0, 0), WATER)
    terrain_maze.set_terrain((5, 5), GRASS)
    terrain_maze.set_terrain((2, 3), TRAP)
    terrain_maze.set_terrain((6, 1), SAND)
    terrain_maze.set_terrain((1, 0), WATER)
    terrain_maze.set_terrain((6, 5), TRAP)
    terrain_maze.set_terrain((3, 3), GRASS)
    terrain_maze.set_terrain((0, 1), SAND)
    terrain_maze.set_terrain((1, 0), WATER)
    terrain_maze.set_terrain((6, 5), GRASS)
    terrain_maze.set_terrain((3, 3), SAND)
    terrain_maze.set_terrain((0, 1), TRAP)
    Visualizer(wall_maze, terrain_maze, start_point, finish_point).render()
    print(start_point, finish_point)
    for i in range(terrain_maze.height):
        for j in range(terrain_maze.width):
            if (i, j) == start_point: print("s", end=" ")
            elif (i, j) == finish_point: print("f", end=" ")
            else: print(terrain_maze.cell_at((i, j)).terrain.in_print, end=" ")
        print()
    for i in range(wall_maze.height):
        for j in range(wall_maze.width):
            if (i, j) == start_point: print("s", end=" ")
            elif (i, j) == finish_point: print("f", end=" ")
            else: print(wall_maze.cell_at((i, j)).terrain.in_print, end=" ")
        print()