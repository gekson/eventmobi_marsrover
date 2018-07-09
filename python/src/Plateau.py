class Plateau:
    valid_directions = ('N', 'E', 'S', 'W')    

    def __init__(self, x_dim = 0, y_dim = 0):
        self.grid = (x_dim, y_dim)
        self.coords = (0, 0)

    def checkValidDirection(direction):
        if direction not in Plateau.valid_directions:
            raise "Invalid Direction Error. 'N', 'E', 'S', 'W'"
    
    def move(self, direction):
        Plateau.checkValidDirection(direction)
        coord_map = {
            Plateau.valid_directions[0]: [self.coords[0], self.coords[1]+1], # N
            Plateau.valid_directions[1]: [self.coords[0]+1, self.coords[1]], # E
            Plateau.valid_directions[2]: [self.coords[0], self.coords[1]-1], # S
            Plateau.valid_directions[3]: [self.coords[0]-1, self.coords[1]]  # W
        }
        new_pos = coord_map.get(direction, None)
        return Plateau.getPosition(new_pos[0], new_pos[1])

    def getPosition(self, x, y):
        if x < 0 or y < 0 or x >= self.grid[0] or y >= self.grid[1]:
            raise "Invalid Coordinate " 
        return (x, y)