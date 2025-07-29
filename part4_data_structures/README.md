# Part IV: Data Structures and Functions/Methods

## Goal
Organize your code using a `Grid` class and methods for robot actions. Introduce a goal tile to win the game.

## Steps
1. Refactor your code to include a `Grid` class that manages:
    - The 2D grid (using a list of lists)
    - Placement of trees ("T"), rocks ("R"), and a goal ("G")
    - Methods for displaying the grid, checking blocked cells, and checking the win condition
2. Update your main loop and robot logic to use these class methods.
3. The robot wins the game by reaching the goal ("G").

## Example Output

Robot is at (4, 4)
Congratulations! You reached the goal!

## Stretch Goals

- Track and display the robot’s path.
- Add collectible items to the grid (e.g., "C").
- Allow the robot to pick up or collect items.
- Display a score for collected items.
- Add more methods to the `Grid` or `Robot` classes for advanced behavior.