import pyxel

class Grid ():
    
    def __init__(self, dimensions : tuple) -> None:
        self.width, self.height = dimensions
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
        pyxel.load (0,0,"Ressources\plateau.png")

    def clear(self) -> None :
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
    
    def insert(self, coordinates, token):
        token.x, token.y = coordinates
        self.grid[token.y][token.x] = token