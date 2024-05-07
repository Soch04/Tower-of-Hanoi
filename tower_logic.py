"""
Towers of Hanoi:
    The game consists of three towers and disks of different
    sizes. The game starts with the disks stacked in tower A, 
    ordered with the smallest at the top.

Brief Instructions:
    The objective of the puzzle is to move the entire stack from 
    the initial rod to another rod.

    Example: To move a disk from tower A to tower B, enter 'AB'.
    To quit the game, enter 'Q'.

Author:
    Sonya C
"""


class Disk:
    """A class to represent a disk in the Towers of Hanoi game.

    Attributes:
        size (int): The size of the disk.

    """

    def __init__(self, size: int):
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
    """A class to represent a tower in the Tower of Hanoi game.

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
        self.disks.insert(0, disk)

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


class Game:
    NUMBER_DISKS: int = 3  # "Number of disks", edit value to change number of disks.

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

        # Push if the target tower is empty OR the top disk in target tower
        # is greater than size of incoming disk.
        elif current_tower.peek() is not None and (
            target_tower.is_empty() or (current_tower.peek() < target_tower.peek())
        ):
            target_tower.push(current_tower.pop())
            print(f"Moved disk to {target_tower.name}")

        else:
            print("No action: Can not add disk")

    @staticmethod
    def print_towers(towers: list[Tower]):
        """Prints the state of all towers.

        Args:
            towers (List[Tower]): A list of all towers.
        """
        for tower in towers:
            for disk in tower.disks:
                print(disk)
            print(tower.name + "\n")

    def setup_game(self) -> None:
        """Sets up the game with towers and disks."""
        self.towerA = Tower("A")
        self.towerB = Tower("B")
        self.towerC = Tower("C")

        self.towers = [self.towerA, self.towerB, self.towerC]

        # Initialize disks and add them to the first tower (A).
        # For loop: Starts at "number of disks", stops at 0, decrements by 1.
        # Change NUMBER_DISKS to change the starting number.
        for size in range(self.NUMBER_DISKS, 0, -1):
            self.towerA.push(Disk(size))

    @staticmethod
    def get_command() -> str:
        """Gets a command from the user. Verifies that the command is only 2 characters, 
        or is the character Q.

        Returns:
            str: The command entered by the user.
        """
        command = input("Move disk? (Q to quit) ").upper()

        while len(command) != 2 and command != "Q":
            command = input("Use only 2 letters ").upper()

        return command

    def execute_command(self, command) -> None:
        """Pushes disks from one tower to another based on a 2-character string input.

        The first character (current tower) is the tower name from which the topmost disk is 
        to move.
        The second character (target tower) is the tower name to which the disk is to be moved.

        Args:
            command (str): A two-character string representing the move command,
                e.g., 'AB' to move top topmost disk from tower A to tower B
        """
        current_tower, target_tower = None, None

        for tower in self.towers:
            # Assign index 0 to corresponding tower name.
            if command[0] == tower.name:  
                current_tower = tower

            # Assign index 1 to corresponding tower name.
            elif (command[1] == tower.name):  
                target_tower = tower

        # If current and target towers are equal to a Tower object (are not set to None),
        # push the current disk to target disk.
        if current_tower and target_tower:
            self.push_disk(target_tower, current_tower)
        else:
            print(f"{command} contains invalid values")

    def is_win(self, towers: list[Tower]) -> bool:
        """Checks if any of the towers, other than the first tower, has all disks, 
        indicating a win.
        """
        for tower in towers[1:]:
            if tower.size() == self.NUMBER_DISKS:  # Win if tower has all disks
                return True

        return False

    def main(self) -> None:
        """Starts the game and handles the game loop."""
        self.setup_game()
        self.print_towers(self.towers)
        command = self.get_command()

        while command != "Q":
            self.execute_command(command)
            self.print_towers(self.towers)

            if self.is_win(self.towers):
                print("You have completed the puzzle!")
                command = "Q"  # Setting command to Q automatically quits the game.
            else:
                command = self.get_command()


if __name__ == "__main__":
    game = Game()
    game.main()
