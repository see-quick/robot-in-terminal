# Part III: If-Else and Error Handling

## Goal
Learn to use `if-else` statements for decision-making and add error handling for invalid moves or commands.

## Steps
1. Print the grid and robot's position.
2. Check for valid commands (`up`, `down`, `left`, `right`, `quit`).
3. Prevent the robot from moving into trees or rocks (block the move, print a message).
4. Prevent the robot from moving outside the grid.
5. Handle unknown commands with an error message.

## Example Output

```
Enter command: up
Move blocked by a tree!
Enter command: fly
Unknown command.
Enter command: left
Can’t move outside the grid.
```

## Stretch Goals
- If the user enters an invalid move, do not advance the game loop; ask again for a command. 
- Track how many invalid commands or blocked moves the user makes, and display a summary at the end.
- Limit the robot to a set number of moves (e.g., 20). Print "Game over" if the moves run out.
- Print a different funny or themed error message each time for invalid input or blocked moves.
- If the user enters `help`, print a short help message showing valid commands.
- Allow commands in any case (e.g., `Up`, `LEFT`, `down`).
- Add a "reset" command to return the robot to the starting position.