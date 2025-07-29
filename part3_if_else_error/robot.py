import random

# TODO: Copy your Robot class here.
# class Robot:
#     ...

# TODO: Write a function to create a grid (2D list filled with ".")
# def create_grid(size):
#     ...

# TODO: Write a function to randomly place trees ("T") and rocks ("R") on the grid
# def place_random(grid, symbol, count, avoid=None):
#     ...

# TODO: Write a function to check if a cell is blocked (tree or rock)
# def is_blocked(grid, x, y):
#     ...

# TODO: Write a function to print the grid, showing robot as "X"
# def print_grid(grid, robot_pos):
#     ...

def main():
    size = 5  # Grid size
    # TODO: Create the grid and robot
    # grid = ...
    # robot = ...
    # avoid = ...   # set of positions to avoid

    # TODO: Place trees and rocks on the grid
    # place_random(grid, 'T', 3, avoid)
    # place_random(grid, 'R', 3, avoid)

    while True:
            # REMOVE pass if you start here
            pass
            # TODO: Print the grid and robot position
            # print_grid(grid, robot.position())
            # print(f"Robot (X) is at {robot.position()}")

            # TODO: Get move command from user (convert to lowercase)
            # cmd = input("Move (up/down/left/right) or 'quit': ").lower()

            # TODO: End the loop if the user types 'quit'
            # if cmd == 'quit':
            #     print("Bye!")
            #     break

            # TODO: Convert command to dx, dy
            # dx, dy = 0, 0
            # if cmd == ...:
            #     ...
            # else:
            #     print("Unknown command.")
            #     continue

            # TODO: Compute the new position
            # nx, ny = robot.x + dx, robot.y + dy

            # TODO: Check if move is off-grid
            # if not (0 <= nx < size and 0 <= ny < size):
            #     print("Can't move outside the grid.")
            #     continue

            # TODO: Check if move is blocked by obstacle
            # if is_blocked(grid, nx, ny):
            #     print("Move blocked by an obstacle!")
            #     continue

            # TODO: If valid, update the robot's position
            # robot.set_position(nx, ny)

if __name__ == "__main__":
    main()