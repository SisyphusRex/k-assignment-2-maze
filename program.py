"""Program code"""

# First-party imports
from maze_solver import MazeSolver
from maze_printer import MazePrinter


def main(*args):
    """Method to run program"""

    # Starting Coordinates
    X_START = 1
    Y_START = 1

    # The first maze that needs to be solved.
    # NOTE: You may want to make a smaller version to test and debug with.
    # You don't have to, but it might make your life easier.
    maze1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    # practice maze
    mazeP = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", "#", ".", ".", "#"],
        ["#", "#", ".", "#", "#"],
    ]
    # Create new instance of a MazeSolver
    maze_solver = MazeSolver()

    # Create the second maze by transposing the first maze
    maze2 = transpose_maze(maze1)

    # Solve the practice maze
    maze_solver.solve_maze(mazeP, X_START, Y_START)
    # Solve the original maze
    # maze_solver.solve_maze(maze1, X_START, Y_START)

    # Solve the transposed maze
    # maze_solver.solve_maze(maze2, X_START, Y_START)


def transpose_maze(maze_to_transpose):
    """This method will take in a 2d list (list of lists) and return a new
    2d list maze that is flipped along the diagonal, or in mathematical terms,
    transposed.

    ie. If the array looks like:
    1, 2, 3
    4, 5, 6
    7, 8, 9
    Then the returned result will be:
    1, 4, 7
    2, 5, 8
    3, 6, 9

    The current return statement is just a placeholder so the program doesn't
    contain any syntax errors. You need to replace this with the work you need
    to do for actually transposing the maze.

    It is important that you make a new 2d list and copy each element from the
    original to the new transposed one. Failure to do so may lead you to only
    be able to solve the transposed one.
    """
    transposed_maze = []
    original_row_count = len(maze_to_transpose)
    original_column_count = len(maze_to_transpose[0])
    new_row_count = original_column_count
    # add number of rows in new maze equal to numer of columns in old maze
    for row in range(new_row_count):
        transposed_maze.append([])
    # append elements from original maze to reverse coordinates
    for row in range(original_row_count):
        for column in range(original_column_count):
            transposed_maze[column].append(maze_to_transpose[row][column])
    return transposed_maze
