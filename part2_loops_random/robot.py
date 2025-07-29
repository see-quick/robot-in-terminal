import random

# TODO: Copy your Robot class from Part I here.
# class Robot:
#     ...

# TODO: Write a function to generate a grid of size N x N (use a 2D list, each cell as ".")
# def create_grid(size):
#     ...

# TODO: Write a function to randomly place trees ("T") and rocks ("R") on the grid
# def place_random(grid, symbol, count, avoid=None):
#     ...

# TODO: Write a function to print the grid, marking the robot as "X" at its position
# def print_grid(grid, robot_pos):
#     ...

def main():
    size = 5  # You can change the grid size
    # TODO: Create a grid of the given size
    # grid = ...

    # TODO: Create a Robot at position (0, 0)
    # robot = ...

    # TODO: Avoid placing objects on the robot's starting spot (optional: use an "avoid" set)
    # avoid = ...

    # TODO: Place trees ("T") and rocks ("R") randomly on the grid
    # place_random(grid, 'T', 3, avoid=avoid)
    # place_random(grid, 'R', 3, avoid=avoid)

    while True:
            # REMOVE pass if you start here
            pass
            # TODO: Print the grid and the robot's current position
            # print_grid(grid, robot.position())
            # print(f"Robot (X) is at {robot.position()}")

            # TODO: Ask the user for a move command (up/down/left/right or quit)
            # cmd = input("Move (up/down/left/right) or 'quit': ")

            # TODO: If the user types "quit", break the loop and end the game
            # if cmd == 'quit':
            #     print("Bye!")
            #     break

            # TODO: Convert command into (dx, dy) movement
            # dx, dy = 0, 0
            # if cmd == ...:
            #     ...

            # TODO: Update the robot's position (no collision checks yet!)
            # nx, ny = robot.x + dx, robot.y + dy
            # if ...:
            #     robot.set_position(nx, ny)
            # else:
            #     print("Can't move outside the grid.")

if __name__ == "__main__":
    main()