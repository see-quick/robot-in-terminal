import random

class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

def create_grid(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def place_random(grid, symbol, count, avoid=None):
    size = len(grid)
    placed = 0
    while placed < count:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        # Avoid placing on forbidden spots
        if grid[y][x] == '.' and (not avoid or (x, y) not in avoid):
            grid[y][x] = symbol
            placed += 1

def print_grid(grid, robot_pos):
    size = len(grid)
    for y in range(size):
        row = ''
        for x in range(size):
            if (x, y) == robot_pos:
                row += 'X '
            else:
                row += grid[y][x] + ' '
        print(row)
    print()

def main():
    size = 5
    grid = create_grid(size)
    robot = Robot(0, 0)

    # Avoid robot's starting spot
    avoid = {(robot.x, robot.y)}

    # Place trees ("T") and rocks ("R")
    place_random(grid, 'T', 3, avoid=avoid)
    place_random(grid, 'R', 3, avoid=avoid)

    while True:
        print_grid(grid, robot.position())
        print(f"Robot (X) is at {robot.position()}")
        cmd = input("Move (up/down/left/right) or 'quit': ")
        if cmd == 'quit':
            print("Bye!")
            break
        dx, dy = 0, 0
        if cmd == 'up':
            dy = -1
        elif cmd == 'down':
            dy = 1
        elif cmd == 'left':
            dx = -1
        elif cmd == 'right':
            dx = 1
        else:
            print("Unknown command.")
            continue

        # No collision/block check yet (that's Part III)
        nx, ny = robot.x + dx, robot.y + dy
        if 0 <= nx < size and 0 <= ny < size:
            robot.set_position(nx, ny)
        else:
            print("Can't move outside the grid.")

if __name__ == "__main__":
    main()