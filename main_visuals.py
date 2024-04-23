"""
This file was made by Francisco Serrano-Robles
this file does the graphics for the towers of hanoi game.
"""

import grid
from  tower_logic import Game, Tower

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
            #pointer is set to right above the letters labeling the towers
            pointer = backdrop.rows - 2
 
            #no one cares for empty towers, this is just an optimization
            if tower.is_empty() == False:
                #instead of doing a more "elbow grease" method I just used my scangridsingular() to find the tower we are looking for
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

        return command


jemmy = graphics()
jemmy.main()
