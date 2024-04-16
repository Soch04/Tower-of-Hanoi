import grid
import pallets

towwy = grid.matrix(6,5,'.')

#write to point takes coords as (Y,X), begining from the top left, and the starting index is (0,0)

towwy.writeToPoint('C',(5,4))
towwy.writeToPoint('B',(5,2))
towwy.writeToPoint('A',(5,0))
towwy.drawGrid(1, pallets.drawkeyHanoi, 'lavender')

print(towwy)
