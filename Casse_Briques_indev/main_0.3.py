"""
A coder :  - éventuelles évolutions
A tester : Tout (comportements de la plateforme, comportements de la balle, rebonds de la balle sur les briques)
Testé : Rien
"""

import pyxel
from Plateforme import Plateforme
from Balle import Balle
from Briques import *
from Levels import Levels

class Jeu:
    def __init__(self):
        
        # taille de la fenetre 128x128 pixels
        # ne pas modifier
        pyxel.init(128, 128, title="Nuit du c0de", fps=60)

        # création de la pateforme
        self.plateforme_1 = Plateforme (20,5)
        
        # création de la balle
        self.balle = Balle(1)

        self.nb_update = 0

        self.current_level = 2

        self.level = Levels(self.current_level)

        self.game_started = False # indicateur de l'état du Jeu (False -> jeu non commencé
                                  #                              True -> jeu commencé)
        
        pyxel.run(self.update,self.draw)

    def start(self): # déclencheur du jeu
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_LEFT):
            self.game_started = True
#======================================================================================================== UPDATE

    def update(self):
        """mise à jour des variables (60 fois par seconde)"""

        if self.game_started: # Tant que le Jeu n'est pas commencé, on attend
            
            self.nb_update += 1

            # deplacement de la plateforme
            self.plateforme_1.deplacement()

            # deplacement de la balle
            self.balle.deplacement(self.nb_update, self.plateforme_1, self.level.current_level)
            
            if self.level.current_level == [] :
                if self.current_level + 1 in self.level.levels:
                    self.current_level += 1
                    self.level = Levels(self.current_level)
        else :
            self.start()
        
        
#======================================================================================================== DRAW

    def draw(self):
        """création et positionnement des objets (60 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        for i in self.level.current_level :
            i.draw()
        
        # plateforme (rectangle 20x5)
        self.plateforme_1.draw()

        # balle (cercle de rayon 1)
        self.balle.draw()

Jeu()