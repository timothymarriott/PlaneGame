from SpriteRegistry import *
from Text import *
from Input import *

class Menu:

    logoPosX = 0
    logoPosY = 0

    buttonTime = 0

    Selected = 0

    changedThisFrame = False

    speed = 20
    buttonSpeed = 1

    def __init__(self) -> None:
        pass

    def Start(self):
        RegisterSprite("logo", "initial_logo.png")
        self.logoPosX = Window.WINDOW._actualWidth / 2
        self.logoPosY = -LoadSprite("logo").get_height() / 2
        
        pass

    def Draw(self):
        DrawSprite("logo", self.logoPosX - LoadSprite("logo").get_width() / 2, self.logoPosY - LoadSprite("logo").get_height() / 2)
        if self.logoPosY < 50:
            self.logoPosY += Window.DeltaTime() * self.speed
            if Input.GetKeyDown(pg.K_SPACE):
                self.logoPosY = 50
                self.buttonTime = self.buttonSpeed * 2
        else:
            self.logoPosY = 50
            self.buttonTime += Window.DeltaTime()

        if self.buttonTime > self.buttonSpeed:
            #DrawSprite("logo", 0, 180)
            
            if self.Selected == 0:
                DrawText("START", Window.WINDOW._actualWidth / 2 - GetTextWidth("START") / 2, 120, (255, 255, 0))
                if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame and self.buttonTime > self.buttonSpeed * 2:
                    self.Selected = 1
                    self.changedThisFrame = True
                if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                    Window.WINDOW._game._player.deathTimer = 0
                    Window.WINDOW._game._player.doRender = True
                    Window.WINDOW._game._player.posX = Window.WINDOW._actualWidth / 2
                    Window.WINDOW._game._player.posY = Window.WINDOW._actualHeight / 2
                    Window.WINDOW._game._enemies.clear()
                    Window.WINDOW._game._bullets.clear()
                    Window.WINDOW._game._explosions.clear()
                    Window.WINDOW._game._enemyBullets.clear()
                    Window.WINDOW._game._background.posY = 0
                    Window.WINDOW._game._score = 0
                    Window.WINDOW._game._waveTime = 5
                    Window.WINDOW._game._wave = 0
                    Window.WINDOW._game._SkipMenu = True
                    Window.WINDOW._game._player.PlayStartAnim()
                    
            else:
                DrawText("START", Window.WINDOW._actualWidth / 2 - GetTextWidth("START") / 2, 120, (255, 255, 255))
        if self.buttonTime > self.buttonSpeed * 2:
            
            if self.Selected == 1:
                DrawText("EXIT", Window.WINDOW._actualWidth / 2 - GetTextWidth("EXIT") / 2, 160, (255, 255, 0))
                if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame:
                    self.Selected = 0
                    self.changedThisFrame = True
                if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                    Window.WINDOW.closed = True
            else:
                DrawText("EXIT", Window.WINDOW._actualWidth / 2 - GetTextWidth("EXIT") / 2, 160, (255, 255, 255))

        self.changedThisFrame = False

        pass

    def Reset(self):
        self.logoPosX = Window.WINDOW._actualWidth / 2
        self.logoPosY = -LoadSprite("logo").get_height() / 2
        self.buttonTime = 0
        self.buttonSpeed = 0.25
        self.speed = 100