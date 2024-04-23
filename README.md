### Credits
- Logic implemented by Sonya Cheteyan
- Visuals implemented by Francisco Serrano-Robles

# Tower of Hanoi:
*Note: The GIF is not from the project.*

![fig3](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/20a2bede-7291-47c1-aabf-59ff697f6e66)

The game consists of at least three towers and disks. All the disks begin on one tower, ordered from largest to smallest, with the largest disk on the bottom. 
The objective of the puzzle is to move all disks from the initial tower to another. 

## The Code:
The following is a brief overview of the code:

**Disks:**
A disk is an object that holds a `size` value. A set value determines the number of disks.
- You may change the number of disks by changing the value of `NUMBER_DISKS` in  `tower_logic` under the class `Game`.

**Tower:**
An object with a `name` value and a list to store all the disks. It is based on a stack data structure, including functions such as `push,` `peek,` and `pop`. 
These functions manipulate disks from one tower to another.

As default, we settled on three tower objects and three disk objects. 

## Gameplay
### Introduction
- The game begins with the disks stacked in tower A, ordered with the smallest at the top.
- Numbers represent disks of different sizes, with three being the largest.
  
The following image is from the project. 

![Screenshot 2024-04-22 190803](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/e11151ed-faee-4104-816e-98761dd65f72)

**Note:** Changed the number of disks from 3 to 4.

![Screenshot 2024-04-22 191951](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/e6d2f0a1-7cb0-4586-a442-5cd1a5e677a0)

### Input

- To move disks, the user must indicate the current tower and the target tower.
  - The user represents this with a string of 2 valid characters representing the towers. This is not case-sensitive.
 
- To quit the game, enter `Q`.

**Example:** To move a disk from tower A to tower B, enter `AB` or  `ab`.

![Screenshot 2024-04-22 190830](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/3d2e7098-aaa7-48d9-84d4-577deb8a2c0b)

### Invalid Input

- The game accounts for invalid input:
  - If the user does not specifically enter two letters will be prompted to retry.
  - If the user enters two letters that do not represent a tower (ex: `XX`), the game will not move a disk.
  - If the user tries to move a disk between valid towers, but the disk on the current tower is larger than the one on the target tower, the game will notify the user.

![Gif for Hanoi](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/c26e6ee7-9718-49bc-ac0f-2d4e8da0701b)

### Winning
- The user wins once they move all disks to a different tower.

![Screenshot 2024-04-22 190909](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/c59f8d0a-65a2-4fb4-ae80-684d1784a175)





