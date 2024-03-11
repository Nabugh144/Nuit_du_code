import pyxel

class Grid ():
    
    def __init__(self, dimensions : tuple) -> None:
        self.width, self.height = dimensions
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
        pyxel.load (0,0,"Ressources\plateau.png")

    def clear(self) -> None :
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
    
    def insert(self, token):

        for y in range (len(self.grid),0,-1) :
            if self.grid[y][token.x] == None :
                token.y = y
                break

        self.grid[token.y][token.x] = token

    def draw(self):
        pass
