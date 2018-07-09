import unittest
from Position import *
from Plateau import *
from Rover import *

class TestRovers(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)

    def testValidDirections(self):
        self.assertEqual(Position.valid_directions[0], "N")

    def testGetPosition(self):
        self.position = Position(2, 2, self.plateau)
        self.assertEqual(Position.getPosition(self,2,2).coords, self.position.coords)

    def testOneStepMoveRover(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.oneStep()
        self.assertEqual(rover.position.coords, (0, 1))
        
    def testTwoStepMoveRover(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.oneStep()
        rover.oneStep()
        self.assertEqual(rover.position.coords, (0, 2))
        
    def testRoverRotateLeft(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.rotateLeft()
        self.assertEqual(rover.direction, "W")
        
    def testRoverRotateRight(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.rotateRight()
        self.assertEqual(rover.direction, "E")
        
    def testRoverRotateRightOneStep(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.rotateRight()
        rover.oneStep()
        self.assertEqual(rover.position.coords, (1, 0))
        
    def testRoverTwoStepRotateRight(self):
        rover = Rover("rover1", 0, 0, "N", self.plateau)
        rover.oneStep()
        rover.oneStep()
        rover.rotateRight()
        self.assertEqual(rover.position.coords, (0, 2))
        self.assertEqual(rover.direction, "E")
        
    def testInstructionsRover(self):
        #Plateau:5 5
        #Rover1 Landing:1 2 N
        #Rover1 Instructions:LMLMLMLMM
        
        rover = Rover("rover1", 1, 2, "N", self.plateau)
        instructions = "LMLMLMLMM"
        
        for this_char in instructions:
            if this_char is 'L':
                rover.rotateLeft()
            elif this_char is 'R':
                rover.rotateRight()
            elif this_char is 'M':
                rover.oneStep()
            else:
                raise "Invalid Intructions: L or R or M"
        
        self.assertEqual(rover.position.coords, (1, 3))
        self.assertEqual(rover.direction, "N")
        
    def testInstructionsTwoRovers(self):
        #Plateau:5 5
        #Rover1 Landing:1 2 N
        #Rover1 Instructions:LMLMLMLMM
        #Rover2 Landing:3 3 E
        #Rover2 Instructions:MMRMMRMRRM
        
        rover1 = Rover("rover1", 1, 2, "N", self.plateau)
        rover1.instructions = "LMLMLMLMM"
        rover2 = Rover("rover2", 3, 3, "E", self.plateau)
        rover2.instructions = "MMRMMRMRRM"
        
        rovers = [rover1, rover2]
        
        for item in rovers:    
            
            for this_char in item.instructions:
                if this_char is 'L':
                    item.rotateLeft()
                elif this_char is 'R':
                    item.rotateRight()
                elif this_char is 'M':
                    item.oneStep()
                else:
                    raise "Invalid Intructions: L or R or M"
        
        self.assertEqual(rover1.position.coords, (1, 3))
        self.assertEqual(rover1.direction, "N")
        
        self.assertEqual(rover2.position.coords, (5, 1))
        self.assertEqual(rover2.direction, "E")
        print('{0}:{1} {2} {3}'.format(rover1.getName(), rover1.getPosition()[0], rover1.getPosition()[1], rover1.getDirection()))
        print('{0}:{1} {2} {3}'.format(rover2.getName(), rover2.getPosition()[0], rover2.getPosition()[1], rover2.getDirection()))

if __name__ == '__main__':
    unittest.main()