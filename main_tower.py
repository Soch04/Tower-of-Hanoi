"""
Towers of Hanoi:
The game consists of three towers and disks of different
sizes. The game starts with the disks 
stacked in tower A, ordered with the smallest at the top.

Brief Instructions:
The objective of the puzzle is to move the entire stack to another rod.

To move a disk from tower A to tower B, enter 'AB'.
To quit the game, enter 'Q'.

Author:
    Sonya C
"""

class Disk:
    """A class to represent a disk in the Towers of Hanoi game.

    Attributes:
        size (int): The size of the disk.

    """
    def __init__ (self, size: int): 
        """Constructs all the necessary attributes for the disk object.

        Args:
            size (int): The size of the disk.
        """
        self.size = size

    def __str__(self) -> str:
        """Returns:
            str: The string representation of the disk size."""
        return str(self.size)

class Tower:
    """A class to represent a tower in the Towers of Hanoi game.

    Attributes:
        disks (list[Disk]): The disks in the tower.
        name (str): The name of the tower.

    """
    def __init__(self, name: str):
        """Constructs all the necessary attributes for the tower object.

        Args:
            name (str): The name of the tower.
        """
        self.disks: list[Disk] = []
        self.name = name

    def is_empty(self) -> bool:
        """Checks if the tower is empty.

        Returns:
            bool: True if the tower is empty, False otherwise.
        """
        return len(self.disks) == 0

    def push(self, disk: Disk) -> None:
        """Adds a disk to the top of the tower.

        Args:
            disk (Disk): The disk to be added.
        """
        self.disks.insert(0,disk)

    def pop(self):
        """Removes the disk at the top of the tower and returns it.

        Returns:
            Disk: The disk that was removed.
        """
        if not self.is_empty():
            temp = self.disks[0]
            del self.disks[0]
            return temp
        else:
            print("Can't pop: Tower is empty")

    def peek(self):
        """
        Returns:
            int: The disk size at the top of the tower.
        """
        if not self.is_empty():
            return self.disks[0].size
        else:
            print("Can't peek: Tower is empty")

    def size(self):
        """
        Returns:
            int: The number of disks in the tower.
        """
        return len(self.disks)
    
class Game():
    @staticmethod
    def push_disk(target_tower: Tower, current_tower: Tower) -> None:
        """Moves a disk from the current tower to the target tower if the move is valid.

        Args:
            target_tower (Tower): The tower to move the disk to.
            current_tower (Tower): The tower to move the disk from.
        """
        # Do not push if there are no disks to push to target tower.
        if current_tower.is_empty():
            print("No action: current tower is empty")
            return 
        
        # Push if disk in target tower is greater than size of incoming disk.
        if current_tower.peek() is not None and (target_tower.is_empty() or (current_tower.peek() < target_tower.peek())):
            target_tower.push(current_tower.pop())
            print(f"Moved disk to {target_tower.name}")

        else:
            print("No action: Can not add disk")

    # PRINT TOWERS
    @staticmethod
    def print_towers(towers: list[Tower]):
        """Prints the state of all towers.

        Args:
            towers (List[Tower]): A list of all towers.
        """
        for tower in towers:
            for disk in tower.disks:
                print(disk)
            print(tower.name+"\n")

    @staticmethod
    def get_input() -> str:
        """Gets a command from the user. Verifies that the command is only 2 characters, or is the character Q.

        Returns:
            str: The command entered by the user.
        """
        command = input("Move disk? (Q to quit) ").upper()

        while len(command) != 2 and command != "Q":
            command = input("Use only 2 letters ").upper()

        return command

    def main(self):
        """Starts the game with a specific amount of towers and disks and handles the game loop.

        """
        towerA = Tower("A")
        towerB = Tower("B")
        towerC = Tower("C")

        towers: list[Tower] = [towerA,towerB,towerC]

        disk1 = Disk(1)
        disk2 = Disk(2)
        disk3 = Disk(3)

        current_tower: Tower 
        target_tower: Tower
        command: str 

        # Add disks to the first tower (A).
        towerA.disks = [disk1,disk2,disk3]

        Game.print_towers(towers)
        command = Game.get_input()

        # MAIN LOOP
        while command != "Q":
            for tower in towers:
                # Assign current tower, index 0 of input
                if command[0] == tower.name:
                    print(f"{tower.name} is current tower")
                    current_tower = tower

                # Assign target tower, index 1 of input
                elif command[1] == tower.name:
                    print(f"{tower.name} is target tower")
                    target_tower = tower
                    
            # Catch exception when the user inputs 2 letters, but not the ones representing the towers.
            try:
                Game.push_disk(target_tower, current_tower)
            except UnboundLocalError:
                print(f"{command} contains invalid values")

            Game.print_towers(towers)
            command = Game.get_input()
    
if __name__ == "__main__":
    game = Game()
    game.main()

