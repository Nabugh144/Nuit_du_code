import pyxel

class Balle ():

    def __init__ (self, rayon):
        
        # position de la balle
        self.ray = rayon
        self.x = 64
        self.x_modifier = 0
        self.x_precedent = 0
        self.y = 122 - rayon
        self.y_modifier = -1
        self.y_precedent = 0
                
    def deplacement (self, nb_update, plateforme, brique):
        
        # départ de la balle à gauche ou à droite
        if nb_update <= 1:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x_modifier = -1
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.x_modifier = 1
        
        # si la balle touche un bord, la balle rebondit

        if self.x == 128 - self.ray or self.x == self.ray : 
            self.x_modifier = -self.x_modifier
        if self.y == self.ray :
            self.y_modifier = -self.y_modifier
        
        #si la balle touche la plateforme, la balle rebondit
        if self.y == 123 - self.ray and self.x >= plateforme.x and self.x <= plateforme.x + plateforme.width:
            self.y_modifier = -self.y_modifier
            #if self.x <= plateforme.x + 14 or self.x >= plateforme.x + 7 :
            #    self.x_modifier = 0
            if self.x <= plateforme.x + 7 :
                self.x_modifier = -1
            if self.x >= plateforme.x + 13 :
                self.x_modifier = 1
            if (self.x >= plateforme.x + 8) and (self.x <= plateforme.x + 12):
                self.x_modifier = 0
        
        # si la balle touche une brique, la faire rebondir
        brique_touchee = None
        
        for i in range(len(brique)) :
            # côté gauche de la brique
            if self.x == brique[i].x - self.ray and self.y >= brique[i].y and self.y <= brique[i].y + brique[i].height and self.x_precedent == brique[i].x - 1 - self.ray:
                self.x_modifier = -self.x_modifier
                brique_touchee = i
            # côté droit de la brique
            elif (self.x == brique[i].x + self.ray + brique[i].width and self.y >= brique[i].y and self.y <= brique[i].y + brique[i].height) and self.x_precedent == brique[i].x + 1 + self.ray + brique[i].width:
                self.x_modifier = -self.x_modifier
                brique_touchee = i
            # côté haut de la brique
            elif (self.y == brique[i].y - self.ray and self.x >= brique[i].x and self.x <= brique[i].x + brique[i].width) and self.y_precedent == brique[i].y - 1 - self.ray:
                self.y_modifier = -self.y_modifier
                brique_touchee = i
            # côté bas de la brique
            elif (self.y == brique[i].y + self.ray + brique[i].height and self.x >= brique[i].x and self.x <= brique[i].x + brique[i].width) and self.y_precedent == brique[i].y + 1 + self.ray + brique[i].height:
                self.y_modifier = -self.y_modifier
                brique_touchee = i

        # si une brique a été touchée, la faire disparaître
        if brique_touchee != None :
            brique.pop(brique_touchee)

        self.y_precedent = self.y
        self.x_precedent = self.x

        self.y += self.y_modifier

        self.x += self.x_modifier

    def draw(self):
        pyxel.circ(self.x, self.y, self.ray, 3)