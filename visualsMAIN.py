"""this makes the game look fire yo
    by FSR
"""

import grid
import pallets
import main_tower

#setting up the towers, these are constant and thus will be constantly referenced.
towwy = grid.matrix(6,5,'.')
towwy.writeToPoint('C',(5,4))
towwy.writeToPoint('B',(5,2))
towwy.feedtoColumn(['.','.','1','2','3','A'],0)

#write to point takes coords as (Y,X), begining from the top left, and the starting index is (0,0)
#these are just for show there is no logic

towwy.drawGrid(1, pallets.drawkeyHanoi, 'brown')

print(towwy)

class graphics(main_tower.Game):
  
    def main(self):
        """Starts the game with a specific amount of towers and disks and handles the game loop.

        """
        towerA = main_tower.Tower ("A")
        towerB = main_tower.Tower ("B")
        towerC = main_tower.Tower ("C")

        towers: list[main_tower.Tower ] = [towerA,towerB,towerC]

        disk1 = main_tower.Disk(1)
        disk2 = main_tower.Disk(2)
        disk3 = main_tower.Disk(3)

        current_tower: main_tower.Tower 
        target_tower: main_tower.Tower 
        command: str 

        # Add disks to the first tower (A).
        towerA.disks = [disk1,disk2,disk3]

        main_tower.Game.print_towers(towers)
        command = main_tower.Game.get_input()

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
                main_tower.Game.push_disk(target_tower, current_tower)
            except UnboundLocalError:
                print(f"{command} contains invalid values")

            main_tower.Game.print_towers(towers)
            command = main_tower.Game.get_input()


jemmy = graphics()
jemmy.main()
