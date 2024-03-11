import pyxel

class Token():

    def __init__(self, color, coordinates) -> None:
        self.color = color
        self.x, self.y = coordinates
        pyxel.load(self.x, self.y, "Ressources\plateau.png")

    def draw() -> None:
        pass
