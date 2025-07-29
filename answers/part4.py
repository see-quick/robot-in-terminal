import random

class Grid:
    def __init__(self, size=5, num_trees=3, num_rocks=3):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.place_random('T', num_trees)
        self.place_random('R', num_rocks)
        self.goal = self.place_random('G', 1)[0]

    def place_random(self, symbol, count):
        placed = 0
        positions = []
        while placed < count:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[y][x] == '.':
                self.grid[y][x] = symbol
                positions.append((x, y))
                placed += 1
        return positions

    def display(self, robot_pos, path=None):
        for y in range(self.size):
            row = ''
            for x in range(self.size):
                if (x, y) == robot_pos:
                    row += 'X '
                elif path and (x, y) in path and self.grid[y][x] == '.':
                    row += '* '
                else:
                    row += self.grid[y][x] + ' '
            print(row)
        print()

    def is_blocked(self, x, y):
        return self.grid[y][x] in ('T', 'R')

    def is_goal(self, x, y):
        return self.grid[y][x] == 'G'

class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path = [(x, y)]  # Stretch: track path

    def position(self):
        return (self.x, self.y)

    def move(self, dx, dy, grid: Grid):
        nx, ny = self.x + dx, self.y + dy
        if not (0 <= nx < grid.size and 0 <= ny < grid.size):
            print("Can't move outside the grid.")
            return False
        if grid.is_blocked(nx, ny):
            print("Move blocked by an obstacle!")
            return False
        self.x, self.y = nx, ny
        self.path.append((self.x, self.y))
        return True

def main():
    grid = Grid(size=5)
    # Ensure robot doesn't start on obstacle/goal
    while True:
        rx, ry = 0, 0
        if not grid.is_blocked(rx, ry) and not grid.is_goal(rx, ry):
            break
        else:
            grid = Grid(size=5)
    robot = Robot(rx, ry)

    print("Reach the goal tile (G) to win!")
    while True:
        grid.display(robot.position(), path=robot.path)
        print(f"Robot is at {robot.position()}")
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

        moved = robot.move(dx, dy, grid)
        if moved and grid.is_goal(robot.x, robot.y):
            grid.display(robot.position(), path=robot.path)
            print(f"Robot is at {robot.position()}")
            print("Congratulations! You reached the goal!")
            break

if __name__ == "__main__":
    main()