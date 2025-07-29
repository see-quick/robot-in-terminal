# Part V (Optional): NPC Strategies

## Goal
Add non-player characters (NPCs) with different movement strategies.

## Steps
1. Create an easy NPC that moves randomly.
2. Create a normal NPC that moves towards the robot.
3. Create a hard NPC that moves twice per turn toward the robot.

## Example Output

```
NPC (easy) moves to (2, 3)
NPC (normal) moves to (1, 1) towards robot
NPC (hard) moves twice to (4, 2) towards robot
```

## Stretch Goals
- Make the robot avoid NPCs.
- Let the NPCs collect items or block the robot.

## Extra Challenge: NPCs Place Obstacles

- Allow NPCs to place rocks or obstacles as they move.
- If an NPC lands on an empty space, there’s a chance it leaves a rock behind.
- The robot (and other NPCs) must avoid these new obstacles.

### Example Output

```
NPC moved to (2, 2) and placed a rock!
Robot tried to move to (2, 2) but hit a rock.
```

## Stretch Goals
- NPCs can only place a limited number of obstacles.
- Allow robot to remove or move rocks.