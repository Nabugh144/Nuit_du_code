import pyxel

class Brique():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 4)