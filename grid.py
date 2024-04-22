"""
This file was made by Francisco Serrano-Robles
this is a multi-purpose matrix class.
it also has a small railway class slapped on it.
"""

#draws a red X with a white background
#default grid item if draw key cannot identify something
def drawNA(pen, crosser):
    pen.color('red')
    pen.fillcolor('white')
    pen.begin_fill()
    corners = []
    for i in range(4):
        pen.forward(50)
        pen.right(90)
        corners.append(pen.pos())
    pen.end_fill()
    width = pen.width()
    crosser.color('red')
    crosser.width(width)
    crosser.up()
    crosser.goto(corners[0])
    crosser.down()
    crosser.goto(corners[2])
    crosser.goto(corners[1])
    crosser.goto(corners[3])
    pen.forward(50)
    pen.color('black')

#go back to start a new row of the grid
def rollback(drawer, origin):

    drawer.up()
    drawer.setx(origin[0])
    drawer.right(90)
    drawer.forward(50)
    drawer.left(90)
    drawer.pencolor('black')
    drawer.fillcolor('black')
    drawer.width(6)
    drawer.down()




#gridlike code
import turtle

## the typical thing when you think graph. a bunch of rows and columns
## each point is initiated upon creation, so no holes. 
## functionally its like graph paper
class matrix:

    def __init__(self, rows, slots, defualtFiller = '#'):
        self.matrix = []
        self.rows = rows
        self.columns = slots
        for row in range(1,rows+1):
            self.matrix.append([])
            for slot in range(1,slots+1):
                self.matrix[row-1].append(defualtFiller)

    #prints grid in a centered fashion
    #for a "classic" (left aligned) print, use fancyprint()
    def __str__(self):
        stringy = ''
        for row in enumerate(self.matrix):
            rowwy = ''
            if row[0] != 0: 
                stringy += '\n'
            for slot in enumerate(self.matrix[row[0]]):
                rowwy += str(slot[1]) + '  '
            rowwy = f"{rowwy : ^100}"
            stringy += rowwy
        stringy += '\n'
        return stringy
    
    #returns the dimensions of the grid, FORMATTED AS (columns, rows)
    def getStats(self):
        return len(self.matrix[0]), len(self.matrix)

    #prints in a crude manner
    def printGrid(self):
        for row in self.matrix:
            print(row)
        print()
    
    #prints in a more refined manner, best used for user view
    #now made redundant with __str__
    def fancyPrint(self):
        for row in enumerate(self.matrix):
            if row[0] != 0: 
                print()
            for slot in enumerate(self.matrix[row[0]]):
                print(slot[1], end = '  ')
        print('\n')

    #writes a stuff to one point exactly
    #expects a tuple for coords
    #coords are (row, column) !!
    def writeToPoint(self, obj, coord):
        self.matrix[coord[0]][coord[1]] = obj
    
    #writes something to a point
    #uses a more standard (x,y)/(column,row) format
    #use this for now on in newer code/programs
    def writeToPointSR(self, obj, coord):
        self.matrix[coord[1]][coord[0]] = obj
    
    #checks a point for specific data, mainly for outsider classes
    #returns a true or false if the obj is at those coords
    #expects a tuple for coords (x,y)
    def examinePoint(self, obj, coord):
        if obj == self.matrix[coord[1]][coord[0]]:
            return True
        else:
            return False

    #fills a row with one character and one character only, basically draws a line
    #indexes start at 0
    def fillToRow(self, obj, row):
        for slot in enumerate(self.matrix[row]):
            self.matrix[row][slot[0]] = obj
    
    #fills a column with one character and one character only, basically draws a line
    #indexes start at 0
    def fillToColumn(self, obj, column):
        for row in enumerate(self.matrix):
            self.matrix[row[0]][column] = obj

    #instead of filling a row with only one character, this takes a list as input to outright replace the target list
    #the only catch is that the feeded list must me the same length as the target list, as to prevent breaks in the size
    def feedToRow(self, lister, row):
        if len(lister) == len(self.matrix[row]):
            self.matrix[row] = lister
        else:
            print('the row and the inserting row are not equal length!! no change made...\n')

    #does feed to row to the entire grid, expects a 2d array as input, also expects same dimensions on both, this doesn't run a check
    #TODO add check cuz I am too lazy too
    def feedToAll(self, arrayArray):
            for lane in enumerate(arrayArray):
               self.matrix[lane[0]].clear()
               for obj in lane[1]:
                    self.matrix[lane[0]].append(obj)

    #same idea as feedToRow, but instead does it to the column. I genuinly do not think this functuion would be 
    #all that useful in terms of data insertion. first thing in the list being inserted will be at row 0 to begin
    def feedtoColumn(self, lister, column):
        if len(lister) == len(self.matrix):
            for row in enumerate(self.matrix):
                self.matrix[row[0]][column] = lister[row[0]]
        else:
            print('the row and the inserting row are not equal length!! no change made...\n')

    #creates a copy of the original matrix, this copy is also a matrix
    def duple(self):
        height = len(self.matrix)
        length = len(self.matrix[0])
        mimic = matrix(height, length)

        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                mimic.writeToPoint(slot[1],(row[0],slot[0]))
        return mimic
    
    #creates an iterable version of the matrix, best used to let other modules look in the matrix for themselves
    #as python doesn't like itterating through this man-made matrix
    def iterable(self):
        mimic = []
        for row in self.matrix:
            mimic.append(row)
        return mimic

    #rotates the grid a clockwise once
    #returns a new grid and doesn't write to the old grid <- IMPORTANT!!
    def rotate(self):
        newGrid = matrix(len(self.matrix),len(self.matrix[0]))

        rottoid = 0
        for row in enumerate(self.matrix):
            newGrid.feedtoColumn(row[1],rottoid-1)
            rottoid -= 1 
        
        return newGrid

    #using turtle, draw the grid
    #uses drawkey as the pallet to use, the drawkey must be a DICT formated as key as the char, and value as the color 
    #if the tile's value doesn't match anything on the drawkey, draws a red rectangle filled with white
    #drawstart sets the pen's beginning location
    #drawstart 0 : begin at origin
    #drawstart 1 : begin at top left corner
    def drawGrid(self, drawstart = 0, drawkey = {}):

        #making the turtle instance

        size = (len(self.matrix[0]), len(self.matrix))
        
        width = size[0] * 50
        length = size[1] * 50

        turtle.bgcolor('black')
        turtle.setup(width * 2,length * 2,0,0)
        turtle.tracer(0)

        #setting the turtle pen 

        pen = turtle.Turtle()
        crosser = turtle.Turtle()
        crosser.up()
        pen.speed(1)
        pen.up()
        if drawstart == 0:
            pen.goto((0,0))
        if drawstart == 1:
            pen.goto((-1*(width/2),length/2))
        origin = pen.pos()
        pen.down()
        pen.width(6)
        pen.fillcolor('black')

        #creating the thing that rolls the turtle back when printing a row

        rollback(pen, origin)

        #the drawing loop
        
        for row in self.matrix:
            for slot in row:
                for key in drawkey:
                    if slot == key:
                        pen.fillcolor(drawkey.get(key))
                        pen.begin_fill()
                        for i in range(5):
                            pen.forward(50)
                            pen.right(90)
                        pen.left(90)
                        pen.end_fill()
                        break
                else:
                    drawNA(pen, crosser)

            
            rollback(pen, origin)
        turtle.mainloop()

    #scans the grid for the desired tile, when found will stop and return the coords of the desired tile
    #if it cannot be found it will return None
    def scanGridSingle(self, target):
        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    return (row[0],slot[0])
        else:
            return None


    #scans the grid for the desired tile, every instance of it found will be added to a list that will be returned
    def scanGridSeveral(self, target):
        hits = set()
        for row in enumerate(self.matrix):
            for slot in enumerate(row[1]):
                if slot[1] == target:
                    hits.add((row[0],slot[0]))
        else:
            return list(hits)



#for the nodey, connections, neighboors, weighted, abstract, tree like mapping of points on a grid
#called rail way for simplicity because it seems fun and easy to get
class railway:

    def __init__(self):
        self.railway = {}
        self.railwaySize = 0
    
    def __str__(self):
        stringy = ''
        stringy += f"{'heres the railway' : ^20}" + '\n'
        for entry in self.railway:
            stringy += f"{entry : ^10}" + str(self.railway[entry])
            stringy += '\n'
        stringy += f"{self.railwaySize : ^ 20}"

        return stringy
    
    #add a node to the railway, if no peramater is givin beyond node name
    #the node added will simply exist without connections
    def addNode(self, nodeName, nodeConnections = []):
        self.railway[nodeName] = set()
        self.railwaySize += 1
        if nodeConnections != None:
            for node in nodeConnections:
                self.railway[nodeName].add(node)
                self.railway[node].add(nodeName)
    
    #adds a connection between pre-existing nodes
    def addConnection(self, Node1, Node2):
        self.railway[Node1].add(Node2)
        self.railway[Node2].add(Node1)
    
    #returns a node's neighboors, if it has any, AS A LIST
    def getConnections(self, node):
        neighboors = self.railway[node]
        if len(neighboors) == 0:
            return None
        else:
            return list(neighboors)

    #does the opposite
    def deleteNode(self, node):
        self.railway.pop(node)
        self.railwaySize -= 1
        for rail in self.railway:
            self.railway[rail].discard(node)

    #does the opposite
    def deleteConnection(self, node1, node2):
        self.railway[node1].discard(node2)
        self.railway[node2].discard(node1)

    #turns a agecency matrix into a railway
    #expects a 2D array of ones and zeros AKA a truth table
    #UNTESED
    def matrixToRail(self, matrix):
        for node in enumerate(matrix):
            print('node')
            print(node)
            hits = []
            for truth in enumerate(node[1]):
                print(truth)
                if truth[1] == 1:
                    hits.append(truth[0])
            print(hits)
            self.railway[node[0]] = set(hits)
            self.railwaySize += 1


#tammy = railway()

#for i in range(10):
#    tammy.addNode(i)

#tammy.addConnection(0,7)

#tammy.addNode(10,[3,2])

#print(tammy)

#tammy.deleteNode(10)
#tammy.deleteConnection(0,7)

#print(tammy)


#mapper.drawGrid(1)

#mapzee = mapper.iterable()
#print(mapzee)

#taffy = railway()

#taffy.matrixToRail(mapzee)

#print(taffy)

#mapper.drawGrid(1)

#DRAW ASSIST

