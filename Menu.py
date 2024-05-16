from SpriteRegistry import *
from Text import *

class Menu:

    logoPosX = 0
    logoPosY = 0

    buttonTime = 0

    def __init__(self) -> None:
        pass

    def Start(self):
        RegisterSprite("logo", "initial_logo.png")
        self.logoPosX = Window.WINDOW._actualWidth / 2
        self.logoPosY = -LoadSprite("logo").get_height() / 2
        LoadChars()
        pass

    def Draw(self):
        DrawSprite("logo", self.logoPosX - LoadSprite("logo").get_width() / 2, self.logoPosY - LoadSprite("logo").get_height() / 2)
        if self.logoPosY < 50:
            self.logoPosY += Window.DeltaTime() * 20
        else:
            self.logoPosY = 50
            self.buttonTime += Window.DeltaTime()

        if self.buttonTime > 1:
            #DrawSprite("logo", 0, 180)
            DrawText("START", Window.WINDOW._actualWidth / 2 - GetTextWidth("START") / 2, 120)
        if self.buttonTime > 2:
            DrawText("EXIT", Window.WINDOW._actualWidth / 2 - GetTextWidth("EXIT") / 2, 160)


        pass


