"""Maze Solver Module"""

# Walter Podewil
# CIS 226
# September 23, 2024

# System Imports

# First Party Imports
from maze_printer import MazePrinter

# Third Party Imports


class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

    # This creates a printer method for use during recursion
    my_printer = MazePrinter()

    def __init__(self):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may wan to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.

        # this attribute saves the exit of the map
        self.exit: tuple = (None, None)
        # this attribute keeps track of whether the maze is solved or not
        self.solving: bool = True

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""
        self.exit = self.__establish_exit(maze)
        self.__maze_traversal(maze, x_start, y_start)
        self.solving = True

    def __maze_traversal(self, maze, current_x, current_y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""

        if self.exit == (current_y, current_x):
            maze[current_y][current_x] = "X"
            self.my_printer.print_maze(maze)
            print("Solved.")
            self.solving = False
            return

        try:
            match maze[current_y][current_x]:
                # First Base Case.
                # If the character is a # then the solver is at a wall and must go back
                case "#":
                    return
                # Movement
                case ".":
                    maze[current_y][current_x] = "X"
                    if self.solving:
                        self.my_printer.print_maze(maze)
                    # move down
                    if self.solving:
                        self.__maze_traversal(maze, current_x, current_y + 1)
                    # move right
                    if self.solving:
                        self.__maze_traversal(maze, current_x + 1, current_y)
                    # move left
                    if self.solving:
                        self.__maze_traversal(maze, current_x - 1, current_y)
                    # move up
                    if self.solving:
                        self.__maze_traversal(maze, current_x, current_y - 1)
                    if self.solving:
                        maze[current_y][current_x] = "O"
                        self.my_printer.print_maze(maze)
                # If the solver lands on an X, go back
                case "X":
                    return
                # If the solver lands on a O, go back
                case "O":
                    return
        except IndexError:
            print("Out of range.")

    def __establish_exit(self, maze: list) -> tuple:
        """This method finds the the exit and returns the row and column"""
        rows = len(maze)
        columns = len(maze[0])
        # check top and bottom of maze for exit
        for column in range(columns):
            if maze[0][column] == ".":
                return 0, column
            if maze[rows - 1][column] == ".":
                return rows - 1, column
        # check left and right for exit
        for row in range(rows):
            if maze[row][0] == ".":
                return row, 0
            if maze[row][columns - 1] == ".":
                return row, columns - 1
        return None, None
