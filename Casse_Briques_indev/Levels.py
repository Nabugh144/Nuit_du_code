import pyxel
from random import randint
from Briques import *

class Levels ():
    def __init__(self, current_level):
            self.levels = { 1 : [Brique(x,y,1) for x in range(4,124,11) for y in range(3,33,6)] , 
                            2 : [Brique(x,y,3) for x in range(4,124,12) for y in range(3,22,6)]
                          }
            self.current_level = self.levels[current_level]