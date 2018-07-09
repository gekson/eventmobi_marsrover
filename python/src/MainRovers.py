from Plateau import *
from Rover import *
from Position import *

def main():
    print("Enter the information of the ships and instructions")
    plateuX, plateuY  = input("Plateu: (X Y) ").split(" ")
    howManyRovers = int(input("How many rovers do you want control? ")) 
    plateau = Plateau(int(plateuX), int(plateuY))

    for item in range(0,howManyRovers):    
        roverX,roverY,roverDirection = input("Landing: (X Y D)").split(" ")   
        instructions = input("Instructions: (LRM)")
        
        rover = Rover("rover"+str(item+1), int(roverX), int(roverY), roverDirection, plateau)
        
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
        
    printPosition(rover)

def printPosition(rover):
    print('{0}:{1} {2} {3}'.format(rover.getName(), rover.getPosition()[0], rover.getPosition()[1], rover.getDirection()))

if __name__ == '__main__':
    main()