class Plateau:
    class InvalidCoordinateError(BaseException):
        def __init__(self):
            pass
    
    def __init__(self, x = 0, y = 0):
        self.grid = (x, y)


    