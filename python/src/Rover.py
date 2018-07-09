from Plateau import *
from Position import *

class Rover:
    instructions = ""
    
    def __init__(self, name, initial_X, initial_Y, initial_direction, plateau):
        Position.checkValidDirection(self, initial_direction)

        self.name = name
        self.initial_X = initial_X
        self.initial_Y = initial_Y
        self.direction = initial_direction
        self.plateau = plateau
        self.position = Position(self.initial_X,self.initial_Y, plateau)
        #print("******",self.direction, "**************")
        #print("INIT******position",self.position, "**************")

    def getPosition(self):
        return self.position.X(), self.position.Y()

    def getDirection(self):
        return self.direction

    def getName(self):
        return self.name
        
    def rotateLeft(self):
        #print("******",self.direction, "**************")
        Rover.rotate(self, True)

    def rotateRight(self):
        Rover.rotate(self, False)

    def rotate(self, is_left = False):
        #print("******",self.position)
        direction_index = Position.valid_directions.index(self.direction)
        if(is_left):
            new_direction = (direction_index - 1)
        else:
            new_direction = (direction_index + 1)
        
        new_direction %= len(Position.valid_directions)
        self.direction = Position.valid_directions[new_direction]
    
    def oneStep(self):
        #print("oneStep******self.position->",self.position)
        self.position = self.position.move(self.direction)
