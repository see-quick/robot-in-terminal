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

    def display(self, robot_pos, npc_positions, path=None):
        for y in range(self.size):
            row = ''
            for x in range(self.size):
                if (x, y) == robot_pos:
                    row += 'X '
                elif (x, y) in npc_positions:
                    row += 'N '
                elif path and (x, y) in path and self.grid[y][x] == '.':
                    row += '* '
                else:
                    row += self.grid[y][x] + ' '
            print(row)
        print()

    def is_blocked(self, x, y, forbidden=None):
        blocked = self.grid[y][x] in ('T', 'R')
        if forbidden and (x, y) in forbidden:
            return True
        return blocked

    def is_goal(self, x, y):
        return self.grid[y][x] == 'G'

    def place_rock(self, x, y):
        if self.grid[y][x] == '.':
            self.grid[y][x] = 'R'

class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path = [(x, y)]

    def position(self):
        return (self.x, self.y)

    def move(self, dx, dy, grid: Grid, npc_positions):
        nx, ny = self.x + dx, self.y + dy
        if not (0 <= nx < grid.size and 0 <= ny < grid.size):
            print("Can't move outside the grid.")
            return False
        if grid.is_blocked(nx, ny, forbidden=npc_positions):
            print("Move blocked by an obstacle or NPC!")
            return False
        self.x, self.y = nx, ny
        self.path.append((self.x, self.y))
        return True

class EasyNPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def move(self, grid: Grid, forbidden):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < grid.size and 0 <= ny < grid.size:
                if not grid.is_blocked(nx, ny, forbidden=forbidden):
                    self.x, self.y = nx, ny
                    # Optionally, randomly place a rock (extra challenge)
                    if random.random() < 0.3:
                        grid.place_rock(self.x, self.y)
                        print(f"NPC (easy) moved to ({self.x}, {self.y}) and placed a rock!")
                    else:
                        print(f"NPC (easy) moves to ({self.x}, {self.y})")
                    return
        # If can't move
        print("NPC (easy) did not move.")

class NormalNPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def move(self, grid: Grid, robot, forbidden):
        rx, ry = robot.position()
        dx = 1 if rx > self.x else -1 if rx < self.x else 0
        dy = 1 if ry > self.y else -1 if ry < self.y else 0
        moves = []
        if dx != 0:
            moves.append((self.x + dx, self.y))
        if dy != 0:
            moves.append((self.x, self.y + dy))
        random.shuffle(moves)  # randomize axis if both possible
        for nx, ny in moves:
            if 0 <= nx < grid.size and 0 <= ny < grid.size:
                if not grid.is_blocked(nx, ny, forbidden=forbidden):
                    self.x, self.y = nx, ny
                    print(f"NPC (normal) moves to ({self.x}, {self.y}) towards robot")
                    return
        print("NPC (normal) did not move.")

class HardNPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def move(self, grid: Grid, robot, forbidden):
        for _ in range(2):  # move two times per turn
            rx, ry = robot.position()
            dx = 1 if rx > self.x else -1 if rx < self.x else 0
            dy = 1 if ry > self.y else -1 if ry < self.y else 0
            moves = []
            if dx != 0:
                moves.append((self.x + dx, self.y))
            if dy != 0:
                moves.append((self.x, self.y + dy))
            random.shuffle(moves)
            moved = False
            for nx, ny in moves:
                if 0 <= nx < grid.size and 0 <= ny < grid.size:
                    if not grid.is_blocked(nx, ny, forbidden=forbidden):
                        self.x, self.y = nx, ny
                        print(f"NPC (hard) moves to ({self.x}, {self.y}) towards robot")
                        moved = True
                        break
            if not moved:
                print("NPC (hard) did not move this step.")

def find_empty(grid, forbidden):
    size = grid.size
    while True:
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        if not grid.is_blocked(x, y, forbidden=forbidden) and not grid.is_goal(x, y):
            return x, y

def main():
    grid = Grid(size=5)
    forbidden = set()
    # Place robot
    rx, ry = find_empty(grid, forbidden)
    robot = Robot(rx, ry)
    forbidden.add((rx, ry))

    # Place NPCs
    ex, ey = find_empty(grid, forbidden)
    npc_easy = EasyNPC(ex, ey)
    forbidden.add((ex, ey))

    nx, ny = find_empty(grid, forbidden)
    npc_normal = NormalNPC(nx, ny)
    forbidden.add((nx, ny))

    hx, hy = find_empty(grid, forbidden)
    npc_hard = HardNPC(hx, hy)
    forbidden.add((hx, hy))

    npcs = [npc_easy, npc_normal, npc_hard]

    print("Reach the goal tile (G) to win! Avoid NPCs (N).")
    while True:
        npc_positions = [npc.position() for npc in npcs]
        grid.display(robot.position(), npc_positions, path=robot.path)
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

        # Robot move (avoid NPCs)
        moved = robot.move(dx, dy, grid, npc_positions)
        if not moved:
            continue
        # Check collision after robot moves
        if robot.position() in npc_positions:
            print("Robot collided with an NPC! Game over.")
            break
        if grid.is_goal(robot.x, robot.y):
            grid.display(robot.position(), [npc.position() for npc in npcs], path=robot.path)
            print(f"Robot is at {robot.position()}")
            print("Congratulations! You reached the goal!")
            break

        # Each NPC moves
        for npc in npcs:
            forbidden = [robot.position()] + [n.position() for n in npcs if n != npc]
            if isinstance(npc, EasyNPC):
                npc.move(grid, forbidden)
            elif isinstance(npc, NormalNPC):
                npc.move(grid, robot, forbidden)
            elif isinstance(npc, HardNPC):
                npc.move(grid, robot, forbidden)
        # Check for collision after NPCs move
        npc_positions = [npc.position() for npc in npcs]
        if robot.position() in npc_positions:
            print("NPC collided with the robot! Game over.")
            break

if __name__ == "__main__":
    main()