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
        # Avoid forbidden cells (e.g., robot start)
        if grid[y][x] == '.' and (not avoid or (x, y) not in avoid):
            grid[y][x] = symbol
            placed += 1

def is_blocked(grid, x, y):
    return grid[y][x] in ('T', 'R')

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
    avoid = {(robot.x, robot.y)}
    place_random(grid, 'T', 3, avoid)
    place_random(grid, 'R', 3, avoid)

    while True:
        print_grid(grid, robot.position())
        print(f"Robot (X) is at {robot.position()}")
        cmd = input("Move (up/down/left/right) or 'quit': ").lower()
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

        nx, ny = robot.x + dx, robot.y + dy

        # Off-grid check
        if not (0 <= nx < size and 0 <= ny < size):
            print("Can't move outside the grid.")
            continue

        # Obstacle check
        if is_blocked(grid, nx, ny):
            print("Move blocked by an obstacle!")
            continue

        robot.set_position(nx, ny)

if __name__ == "__main__":
    main()