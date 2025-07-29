import random

# TODO: Copy or import your Grid and Robot classes here.

# TODO: Define an abstract base class or a generic NPC class (optional, for extension).

# TODO: Define an EasyNPC class:
#   - Moves randomly on the grid each turn
class EasyNPC:
    def __init__(self, x, y):
        # TODO: Store NPC position
        pass

    def position(self):
        # TODO: Return (x, y) tuple
        pass

    def move(self, grid):
        # TODO: Move randomly to an adjacent, non-blocked cell
        pass

# TODO: Define a NormalNPC class:
#   - Moves one step per turn towards the robot (greedy)
class NormalNPC:
    def __init__(self, x, y):
        pass

    def position(self):
        pass

    def move(self, grid, robot):
        # TODO: Move towards the robot's position (one step)
        pass

# TODO: Define a HardNPC class:
#   - Moves two steps per turn towards the robot
class HardNPC:
    def __init__(self, x, y):
        pass

    def position(self):
        pass

    def move(self, grid, robot):
        # TODO: Move two times towards the robot (may call move logic twice)
        pass

# TODO: (Stretch) Allow NPCs to leave rocks/obstacles as they move

# TODO: In your main loop:
def main():
    # TODO: Create grid, robot, and one or more NPCs at random empty locations
    # TODO: Each turn, robot moves, then each NPC moves (and possibly places obstacles)
    # TODO: Print positions and actions for all NPCs
    # TODO: Prevent robot from moving into NPCs, and vice versa
    # TODO: End the game if the robot collides with an NPC, or reaches the goal
    pass

if __name__ == "__main__":
    main()