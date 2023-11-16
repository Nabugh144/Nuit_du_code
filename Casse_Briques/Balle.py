import pyxel
from Briques import Brique

class Balle ():
    
    def __init__ (self, rayon):
        
        # position de la balle
        self.ray = rayon
        self.x = 64
        self.y = 122 - rayon
        self.x_modifier = 0
        self.y_modifier = -1

    @property
    def brique_touchee(self):
        if self.brique

    def deplacement (self, nb_update, plateforme_x):
        if nb_update <= 1:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x_modifier = -1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.x_modifier = 1
        
        if self.x == 128 - self.ray or self.x == self.ray :
            self.x_modifier = -self.x_modifier
        if self.y == self.ray :
            self.y_modifier = -self.y_modifier
        if self.y == 123 - self.ray and self.x >= plateforme_x and self.x <= plateforme_x + 20:
            self.y_modifier = -self.y_modifier
        self.y += self.y_modifier

        self.x += self.x_modifier

        
