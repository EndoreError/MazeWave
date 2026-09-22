from src.maze_generator import MazeGenerator
from src.terrain import WALL

def print_maze(maze_to_print, start_point, finish_point) -> None:
    """ Печатает лабиринт символами в консоль"""
    for r in range(maze_to_print.height):
        line = []
        for c in range(maze_to_print.width):
            if (r, c) == start_point:
                line.append("S")
            elif (r, c) == finish_point:
                line.append("F")
            elif maze_to_print.cell_at((r, c)).terrain == WALL:
                line.append("#")
            else:
                line.append(" ")
        print(" ".join(line))


if __name__ == "__main__":
    maze, start, finish = MazeGenerator(width=10, height=30, seed=98520864).generate_dfs()
    print(f"Лабиринт {maze.width}x{maze.height}")
    print_maze(maze, start, finish)