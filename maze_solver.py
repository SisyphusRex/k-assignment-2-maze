"""Maze Solver Module"""



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

        # this attribute keeps track of whether the maze is solved or not
        self.solving: bool = True

        # this attribute saves the bottom row index and
        self.bounds = {}

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""

        self.bounds = self.__establish_bounds(maze)

        self.__maze_traversal(maze, x_start, y_start)

        # I must reset the bool here to reuse the maze_solver instance later
        self.solving = True

    def __maze_traversal(self, maze, current_x, current_y):
        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""

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

                    # base case.  if solver is on edge of maze, it returns
                    if current_y in (self.bounds["top"], self.bounds["bottom"]):
                        self.solving = False
                        return
                    if current_x in (self.bounds["left"], self.bounds["right"]):
                        self.solving = False
                        return

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

    def __establish_bounds(self, maze: list) -> dict:
        """This method establishes the maze bounds"""
        rows = len(maze)
        columns = len(maze[0])
        left = 0
        right = columns - 1
        top = 0
        bottom = rows - 1
        return {"left": left, "right": right, "top": top, "bottom": bottom}
