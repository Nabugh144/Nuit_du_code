import pyxel

class Plus_2_balles():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.y_modifier = -1
        pyxel.load ("Ressources\Briques.pyxres")

    def deplacement(self):
        
        if self.y == 123 - self.ray and self.x >= plateforme.x and self.x <= plateforme.x + plateforme.width: # si la balle touche la plateforme
            pass

        self.y += self.y_modifier

        
    def draw(self):
        pyxel.blt(self.x, self.y, 0,8,0,10,5)