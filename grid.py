#matrix code
import copy

class matrix:

    def __init__(self, rows, slots, defualtchar = '#'):
        self.matrix = []
        for row in range(1,rows+1):
            self.matrix.append([])
            for slot in range(1,slots+1):
                self.matrix[row-1].append(defualtchar)

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

    #writes a character to one point exactly
    def writeToPoint(self, obj, coord):
        self.matrix[coord[0]][coord[1]] = obj
    
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

    #flips the grid either laterally or vertically
    #direction expects either a "horo" or a "vert"
    #TODO get this working
    def flip(self, direction):
        if direction == 'horo':
            pass
        if direction == 'vert':
            pass
        pass









#mapper = matrix(5,5,'O')

#mapper.fillToRow('T',0)
#mapper.fillToRow('o',1)
#mapper.fillToRow('p',2)
#mapper.fillToRow('p',3)
#mapper.fillToRow('p',4)