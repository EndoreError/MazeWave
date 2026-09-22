from src.MazeGenerator import *

def print_maze(maze, start, finish) -> None:
    """Печатает лабиринт символами: # — стена, . — проход, S — старт, F — финиш."""
    for r in range(maze.height):
        line = []
        for c in range(maze.width):
            if (r, c) == (start[0] * 2 + 1, start[1] * 2 + 1):
                line.append("S")
            elif (r, c) == (finish[0] * 2 + 1, finish[1] * 2 + 1):
                line.append("F")
            elif maze.cell_at(r, c).is_wall:
                line.append("#")
            else:
                line.append(".")
        print(" ".join(line))


if __name__ == "__main__":
    mazeHollow = MazeGenerator(width=10, height=10, seed=29445)
    maze, start, finish = mazeHollow.generateDFS()
    print(f"Лабиринт {maze.width}x{maze.height}, seed=12345")
    print_maze(maze, start, finish)