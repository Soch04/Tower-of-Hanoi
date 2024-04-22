"""this makes the game look fire yo
    by FSR
"""

import grid
#currently unsed pallets but that is because i would need to rework my drawing method...
import pallets
from  main_tower import Game, Tower

# #setting up the towers, these are constant and thus will be constantly referenced.
backdrop = grid.matrix(6,5,'.')
backdrop.writeToPoint('C',(5,4))
backdrop.writeToPoint('B',(5,2))
backdrop.feedtoColumn(['.','.','.','.','.','A'],0)

# #write to point takes coords as (Y,X), begining from the top left, and the starting index is (0,0)
# #these are just for show there is no logic

# backdrop.drawGrid(1, pallets.drawkeyHanoi, 'brown')

#print(backdrop)


class graphics(Game):
      
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
                command = "Q" # Setting command to Q automatically quits the game.
            else:
                command = self.get_command()

      @staticmethod
      def print_towers(towers: list[Tower]):
        """Prints the state of all towers.

        Args:
            towers (List[Tower]): A list of all towers.
        """

        # this stores the data of where the disks will be drawn. it stores it as short lists of [disk.size,tower it is on]
        drawingdisk = []

        for tower in towers:
            #pointer is used to easily keep track of positions on the tower when iterating through them
            pointer = backdrop.rows - 2
            #print(pointer)
            #no one cares for empty towers, this is just an optimization
            if tower.is_empty() == False:
                #instead of doing a more "elbow grease" method I just used my scangridsingular to find the toweer we are looking for
                #from there we have the coords of it on the background, we mainly just want what column its in to place the blocks.
                currenttow = backdrop.scanGridSingle(tower.name)
                for block in reversed(tower.disks):
                    
                    drawingdisk.append([block.size,[pointer,currenttow[1]]])
                    pointer -= 1
        
        #image is what is actual printed, backdrop is kept as place holder so we can have a constant reference to the ABC and grid
        image = backdrop.duple()
        for item in drawingdisk:
            image.writeToPoint(*item)
        
        print(image)


      # this goes cucrenlty unchanged until I really fix up my graphical method for grid...
      @staticmethod
      def get_command() -> str:
        """Gets a command from the user. Verifies that the command is only 2 characters, or is the character Q.

        Returns:
            str: The command entered by the user.
        """
        command = input("Move disk? (Q to quit) ").upper()

        while len(command) != 2 and command != "Q":
            command = input("Use only 2 letters ").upper()

        return command


jemmy = graphics()
jemmy.main()
