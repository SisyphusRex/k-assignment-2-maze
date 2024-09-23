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

    def __init__(self):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may wan to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.
        pass

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""
        self.__maze_traversal(maze, x_start, y_start)
        pass

    def __maze_traversal(self, maze, current_x, current_y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""
        try:
            match maze[current_x][current_y]:
                case "#":
                    # What happens when I hit the wall?
                    ...
                case ".":
                    # what happens when I find a good next step?
                    ...
                case MazePrinter.my_x:
                    # what happens when I hit a previous path
                    ...
                case MazePrinter.my_o:
                    # what happens when I hit a bad path
                    ...

        except IndexError:
            """Game Over Baseline"""
            # if the recursion reaches a point where it is in a valid space yet is trying
            # to move to a space outside the range of the maze lists
            # then it has found the exit.

        pass
