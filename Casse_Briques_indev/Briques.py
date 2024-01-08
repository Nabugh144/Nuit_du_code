import pyxel

class Brique():

    def __init__(self, x, y, hardness):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.hardness = hardness
        pyxel.load ("Ressources\Briques.pyxres")
        self.textures = {
            1 : (self.x, self.y, 0,24,0,10,5),
            2 : (self.x, self.y, 0,12,0,10,5),
            3 : (self.x, self.y, 0,0,0,10,5)
        }
    
    def draw(self):
        (x,y,img,u,v,w,h) = self.textures[self.hardness]
        pyxel.blt(x,y,img,u,v,w,h)
        #pyxel.rect(self.x, self.y, self.width, self.height, self.hardness)