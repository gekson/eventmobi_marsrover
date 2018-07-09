from Plateau import *
from Rover import *

def main():
    print("Enter the information of the ships and instructions")
    plateuX, plateuY  = input("Plateu: (X Y) ").split(" ")
    manyRovers = int(input("How many rovers do you want control? ")) 
    plateau = Plateau(plateuX, plateuY)

    for item in range(0,manyRovers):    
        roverX,roverY,roverDirection = input("Landing: (X Y D)").split(" ")   
        instructions = input("Instructions: (LRM)")
        
        rover = Rover("rover"+str(item), roverX, roverY, roverDirection)
        
        executeRoverInstructions(rover, instructions)

def executeRoverInstructions(rover, instructions):
    try:
        for this_char in instructions:
            if this_char is 'L':
                rover.rotateLeft()
            elif this_char is 'R':
                rover.rotateRight()
            elif this_char is 'M':
                rover.oneStep()
            else:
                raise "Invalid Intructions: L or R or M"
    except Plateau.InvalidCoordinateError:
        print('Rover tried to drive off the plateau!')

if __name__ == '__main__':
    main()