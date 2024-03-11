import pyxel
from Grid import Grid
from Token import Token

class Jeu():
    
    def __init__(self) -> None:
        pyxel.init(692, 692, title="Puissance 4", fps=60)
        self.grid = Grid()
        self.current_color = "Jaune"
        self.token = Token(self.current_color, (0,0))

        self.run(self.update, self.draw)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pyxel.cls(0)
        self.grid.draw()

    def key_pressed(self):
        if pyxel.KEY_RIGHT :
            if self.token.x != 6:
                self.token.x += 1
        if pyxel.KEY_LEFT :
            if self.token.x != 0 :
                self.token.x -= 1
        if pyxel.KEY_KP_ENTER :
            
            self.grid.insert(self.token)

            if self.current_color == "Jaune" :
                self.current_color = "Rouge"
            else : self.current_color = "Jaune"

Jeu()