import pyxel

class Plateforme():

    def __init__(self, width : int, height : int):

        # dimensions de la plateforme
        self.width = width
        self.height = height

        # position initiale de la plateforme
        # (origine des positions : coin haut gauche)
        self.x = 64 - self.width / 2
        self.y = 128 - self.height

    def deplacement (self):

        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < 128 - self.width:
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
            self.x += -1