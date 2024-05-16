from SpriteRegistry import *

class Menu:

    def __init__(self) -> None:
        pass

    def Start(self):
        LoadSprite("logo", "initial_logo.png")
        pass

    def Draw(self):
        DrawSprite("logo", 0, 0, 0)
        pass


