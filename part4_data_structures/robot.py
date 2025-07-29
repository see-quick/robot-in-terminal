import random

# TODO: Define a Grid class
class Grid:
    # TODO: Add a constructor that:
    #   - Sets up the grid size (default 5)
    #   - Creates a 2D grid (list of lists) filled with "."
    #   - Places trees ("T"), rocks ("R"), and a goal ("G") at random locations
    def __init__(self, size=5, num_trees=3, num_rocks=3):
        pass

    # TODO: Add a method to place random objects (trees/rocks/goal) on the grid
    def place_random(self, symbol, count):
        pass

    # TODO: Add a method to display the grid
    #   - Mark the robot as "X"
    #   - Optionally, show the path taken by the robot as "*"
    def display(self, robot_pos, path=None):
        pass

    # TODO: Add a method to check if a cell is blocked (tree or rock)
    def is_blocked(self, x, y):
        pass

    # TODO: Add a method to check if a cell is the goal
    def is_goal(self, x, y):
        pass

# TODO: Define a Robot class
class Robot:
    # TODO: Add a constructor that sets the starting position and tracks the path
    def __init__(self, x=0, y=0):
        pass

    # TODO: Add a method to get the current position as a tuple (x, y)
    def position(self):
        pass

    # TODO: Add a method to move the robot (check for walls and obstacles using Grid methods)
    #   - Only move if not blocked and not outside the grid
    #   - Track the path if move is successful
    def move(self, dx, dy, grid: Grid):
        pass

# TODO: In your main loop:
def main():
    # TODO: Create a Grid object
    # TODO: Ensure the robot starts on an empty tile (not blocked or goal)
    # TODO: Create a Robot object

    # TODO: Print instructions to the user
    while True:
        # TODO: Display the grid (marking robot, path)
        # TODO: Print the robot's current position
        # TODO: Ask user for a move command (up, down, left, right, quit)
        # TODO: Convert command to dx/dy
        # TODO: Use Robot's move method to attempt the move
        # TODO: If robot reaches the goal, display win message and break
        # TODO: End loop on "quit"
        pass

if __name__ == "__main__":
    main()