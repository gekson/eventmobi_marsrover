from Plateau import *

class Rover:
    def __init__(self, name, initial_X, initial_Y, initial_direction):
        Plateau.checkValidDirection(initial_direction)

        self.name = name
        self.initial_X = initial_X
        self.initial_Y = initial_Y
        self.direction = initial_direction
        self._test = "Testando"

    def rotateLeft(self):
        Rover.rotate(True)

    def rotateRight(self):
        Rover.rotate(False)

    def rotate(self, is_left = False):
        print("******",self._test)
        direction_index = Plateau.valid_directions.index(self.direction)
        if(is_left):
            new_direction = (direction_index - 1)
        else:
            new_direction = (direction_index + 1)
        
        new_direction %= len(Plateau.valid_directions)
        self.direction = Plateau.valid_directions[new_direction]
    
    def oneStep(self):
        self._position = self._position.fromHere(self._bearing)
