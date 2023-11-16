"""
A coder : - briques (comportement, emplacements, etc.)
          - éventuelle évolutions
A tester : Tout (comportement de la plateforme, comportement de la balle)
Testé : Rien
================================================= Problèmes ======================================================
Problèmes connus : #2 A faibles fps ou avec une pression sur la flèche trop rapide, la balle part tout droit.
Raison(s) :
Solution(s) envisagée(s) : #2 augmenter le nombre de fps mais cela accelererait le jeu
Problèmes résolus : #1 Le comportement de la balle n'est défini que dans le fichier ""Balle.py""  
"""

import pyxel
from Plateforme import Plateforme
from Balle import Balle
from Briques import Brique

class Jeu:
    def __init__(self):
        
        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="Nuit du c0de")

        # création de la pateforme
        self.plateforme_1 = Plateforme (20,5)

        # création de la balle
        self.balle = Balle(2)

        self.nb_update = 0

        level_1 = {}
        level = [Brique(x,y) for x in range(0,120,10) for y in range(0,115,5)]
        for i in range(len(level)):
            level_1['brique_' + str(i)] = level[i]
        print(level_1)

        self.level_1 = [Brique(x,y) for x in range(0,120,10) for y in range(0,115,5)]

        self.game_started = False # indicateur de l'état du Jeu (False -> jeu non commencé
                                  #                              True -> jeu commencé)
        
        pyxel.run(self.update,self.draw)

    def start(self): # déclencheur du jeu
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT):
            self.game_started = True
#======================================================================================================== UPDATE

    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        if self.game_started: # Tant que le Jeu n'est pas commencé, on attend
            
            self.nb_update += 1

            # deplacement de la plateforme
            self.plateforme_1.deplacement()

            self.balle.game_started = self.game_started

            # deplacement de la balle
            self.balle.deplacement(self.nb_update, self.plateforme_1.x)

            self.balle.brique_touchee


        else :
            self.start()
        
        
#======================================================================================================== DRAW

    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        for i in self.level_1 :
            pyxel.rect(i.x, i.y, i.width, i.height, 4)
            pyxel.rectb(i.x, i.y, i.width, i.height, 7)
        
        # vaisseau (carre 20x5)
        pyxel.rect(self.plateforme_1.x, self.plateforme_1.y, 20, 5, 1)

        # balle (cercle de rayon 1)
        pyxel.circ(self.balle.x, self.balle.y, self.balle.ray, 3)

Jeu()