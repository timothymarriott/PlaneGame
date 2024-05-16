from SpriteRegistry import *

class Menu:

    def __init__(self) -> None:
        pass

    def Start(self):
        RegisterSprite("logo", "initial_logo.png")
        pass

    def Draw(self):
        DrawSprite("logo", 0, 0)
        pass


