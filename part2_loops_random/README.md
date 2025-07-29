# Part II: Loops, Random, and Environment Objects

## Goal
Use loops and random generation to move the robot and create trees and rocks on the grid.

## Tasks
- Complete all TODOs in `robot.py`.

## Steps
1. Create a grid (e.g., 5x5) as a 2D list.
2. Place trees ("T") and rocks ("R") at random positions (use `random`).
3. Place the robot at its starting position and mark it with "X" on the grid.
4. Use a loop to let the user enter move commands, updating the grid and robot position each time.
5. Print the grid and robot position after each move.
6. End when user types "quit".

## Example Output

```
Grid:
X . T . .
. R . . .
. . R . .
Robot (i.e., X) is at (0, 0)
```

## Stretch Goals
- Let the robot pick up or avoid objects.
- Prevent rocks/trees from being placed on the robot’s starting tile.
- Add random placement of a “goal” tile (`G`) for the robot to reach.