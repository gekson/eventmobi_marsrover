from Plateau import *

class Position:

    valid_directions = ('N', 'E', 'S', 'W')

    def __init__(self, x, y, plateau):
        self.plateau = plateau
        self.coords = (x, y)

    def X(self):
        return self.coords[0]

    def Y(self):
        return self.coords[1]

    def checkValidDirection(self, direction):
        if direction not in Position.valid_directions:
            raise "Invalid Direction Error. 'N', 'E', 'S', 'W'"
    
    def move(self, direction):
        Position.checkValidDirection(self, direction)
        
        #COORDINATES - N E S W
        coord_map = {
            Position.valid_directions[0]: [self.coords[0], self.coords[1]+1], 
            Position.valid_directions[1]: [self.coords[0]+1, self.coords[1]], 
            Position.valid_directions[2]: [self.coords[0], self.coords[1]-1], 
            Position.valid_directions[3]: [self.coords[0]-1, self.coords[1]]  
        }
        new_pos = coord_map.get(direction, None)
        return Position.getPosition(self, new_pos[0], new_pos[1])

    def getPosition(self, x, y):
        if (x < 0 or y < 0) or (x > self.plateau.grid[0] or y > self.plateau.grid[1]):
            raise "Invalid Coordinate " 
        return Position(x, y, self.plateau)