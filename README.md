### Credits
- Code logic and README written by Sonya Cheteyan
- Visuals for the towers implemented by Francisco Serrano-Robles

# Tower of Hanoi:
*Note: The GIF is not from the project.*

![fig3](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/20a2bede-7291-47c1-aabf-59ff697f6e66)

The game consists of at least three towers and disks. All the disks begin on one tower, ordered from largest to smallest, with the largest disk on the bottom. 
The objective of the puzzle is to move all disks from the initial tower to another. 

## The Code:
The following is a brief overview of the code:

### Objects:
**Disks:**
A disk is an object that holds a `size` value. A set value determines the number of disks.
- You may change the number of disks by changing the value of `NUMBER_DISKS` in  `tower_logic` under the class `Game`.

**Tower:**
An object with a `name` value and a list to store all the disks. It is based on a stack data structure, including functions such as `push,` `peek,` and `pop`. 
These functions manipulate disks from one tower to another.

As default, we settled on three tower objects and three disk objects. 

### Visuals:
A background is created for towers A, B, and C.

Visuals are done by iterating through each tower object and checking for disks. When all discs are identified, they are drawn accordingly onto the background.

### Logic:
#### Setup:
- The game is set up by creating a set number of tower objects and discs
- The towers are put into a list.

#### Game Loop:
1. The game prints the current tower and disc arrangement and waits for the user to input a two-character string (ex: `AB`). 
2. The game iterates through the `Tower` list, attempting to match the given characters with a tower `name`.
   - The first index of the string is assigned as the `current_tower`
   - The second index of the string is assigned as the `target_tower`
3. The game pushes the topmost disk from the `current_tower` to the `target_tower` ONLY IF both the `current_tower` and `target_tower` exist (meaning that the characters existed as tower names).
4. The game prints the towers and disk arrangement to the screen.
5. The game checks if the user wins.
6. The loop continues until the user wins or presses `Q`.

## Gameplay
### Introduction
- The game begins with the disks stacked in tower A, ordered with the smallest at the top.
- Numbers represent disks of different sizes, with three being the largest.
  
The following image is from the project:

![Screenshot 2024-04-22 190803](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/e11151ed-faee-4104-816e-98761dd65f72)

**Note:** Changed the number of disks from 3 to 4:

![this](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/35ddc56d-c279-40df-a119-ec961144997b)


### Input

- To move disks, the user must indicate the current tower and the target tower.
  - The user represents this with a string of 2 valid characters representing the towers. This is not case-sensitive.
 
- To quit the game, enter `Q`.

**Example:** To move a disk from tower A to tower B, enter `AB` or  `ab`.

![Screenshot 2024-04-22 190830](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/3d2e7098-aaa7-48d9-84d4-577deb8a2c0b)

### Invalid Input

- The game accounts for invalid input:
  - If the user does not specifically enter two letters, the game will prompt them to retry.
  - If the user enters two letters that do not represent a tower (ex: `XX`), the game will not move a disk.
  - If the user tries to move a disk between valid towers, but the disk on the current tower is larger than the one on the target tower, the game will notify the user.
    
GIF demonstrating input handling:

![Gif for Hanoi](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/c26e6ee7-9718-49bc-ac0f-2d4e8da0701b)

### Winning
- The user wins once they move all disks to a different tower.

![Screenshot 2024-04-22 190909](https://github.com/Soch04/Tower-of-Hanoi/assets/79487467/c59f8d0a-65a2-4fb4-ae80-684d1784a175)





