import grid
import pallets

#setting up the towers, these are constant and thus will be constantly referenced.
towwy = grid.matrix(6,5,'.')
towwy.writeToPoint('C',(5,4))
towwy.writeToPoint('B',(5,2))
towwy.feedtoColumn(['.','.','1','2','3','A'],0)

#write to point takes coords as (Y,X), begining from the top left, and the starting index is (0,0)
#these are just for show there is no logic

towwy.drawGrid(1, pallets.drawkeyHanoi, 'lavender')

print(towwy)
