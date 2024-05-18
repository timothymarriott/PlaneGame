from SpriteRegistry import *
from Text import *
from Input import *
from Program import app_folder

class Menu:

    logoPosX = 0
    logoPosY = 0

    buttonTime = 0

    Selected = 0

    changedThisFrame = False

    speed = 20
    buttonSpeed = 1

    inSettings = False

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
                self.buttonTime = self.buttonSpeed * 3
                self.changedThisFrame = True
        else:
            self.logoPosY = 50
            self.buttonTime += Window.DeltaTime()

        if not self.inSettings:

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
                        Window.WINDOW._game._collisionEnemies.clear()
                        Window.WINDOW._game._enemyBullets.clear()
                        Window.WINDOW._game._background.posY = 0
                        Window.WINDOW._game._score = 0
                        Window.WINDOW._game._waveTime = 2
                        Window.WINDOW._game._wave = 0
                        Window.WINDOW._game._SkipMenu = True
                        Window.WINDOW._game._player.PlayStartAnim()
                        
                else:
                    DrawText("START", Window.WINDOW._actualWidth / 2 - GetTextWidth("START") / 2, 120, (255, 255, 255))
            if self.buttonTime > self.buttonSpeed * 2:
                
                if self.Selected == 1:
                    DrawText("SETTINGS", Window.WINDOW._actualWidth / 2 - GetTextWidth("SETTINGS") / 2, 160, (255, 255, 0))
                    if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame and self.buttonTime > self.buttonSpeed * 3:
                        self.Selected = 2
                        self.changedThisFrame = True
                    if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                        self.inSettings = True
                        self.Selected = 0
                else:
                    DrawText("SETTINGS", Window.WINDOW._actualWidth / 2 - GetTextWidth("SETTINGS") / 2, 160, (255, 255, 255))
            
            if self.buttonTime > self.buttonSpeed * 3:
                
                if self.Selected == 2:
                    DrawText("EXIT", Window.WINDOW._actualWidth / 2 - GetTextWidth("EXIT") / 2, 200, (255, 255, 0))
                    if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame:
                        self.Selected = 0
                        self.changedThisFrame = True
                    if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                        Window.WINDOW.closed = True
                else:
                    DrawText("EXIT", Window.WINDOW._actualWidth / 2 - GetTextWidth("EXIT") / 2, 200, (255, 255, 255))

            
        else:
            if self.Selected == 0:
                DrawText("BACK", Window.WINDOW._actualWidth / 2 - GetTextWidth("BACK") / 2, 120, (255, 255, 0))
                if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame:
                    self.Selected = 1
                    self.changedThisFrame = True
                if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                    self.inSettings = False
            else:
                DrawText("BACK", Window.WINDOW._actualWidth / 2 - GetTextWidth("BACK") / 2, 120, (255, 255, 255))

            if Window.WINDOW._game._Muted:

                if self.Selected == 1:
                    DrawText("MUTE: YES", Window.WINDOW._actualWidth / 2 - GetTextWidth("MUTE: YES") / 2, 160, (255, 255, 0))
                    if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame:
                        self.Selected = 0
                        self.changedThisFrame = True
                    if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                        Window.WINDOW._game._Muted = not Window.WINDOW._game._Muted
                else:
                    DrawText("MUTE: YES", Window.WINDOW._actualWidth / 2 - GetTextWidth("MUTE: YES") / 2, 160, (255, 255, 255))
            else:
                if self.Selected == 1:
                    DrawText("MUTE: NO", Window.WINDOW._actualWidth / 2 - GetTextWidth("MUTE: NO") / 2, 160, (255, 255, 0))
                    if Input.GetKeyDown(pg.K_SPACE) and not self.changedThisFrame:
                        self.Selected = 0
                        self.changedThisFrame = True
                    if Input.GetKeyDown(pg.K_RETURN) and not self.changedThisFrame:
                        Window.WINDOW._game._Muted = not Window.WINDOW._game._Muted
                        
                else:
                    DrawText("MUTE: NO", Window.WINDOW._actualWidth / 2 - GetTextWidth("MUTE: NO") / 2, 160, (255, 255, 255))

        self.changedThisFrame = False

        pass

    def Reset(self):
        self.logoPosX = Window.WINDOW._actualWidth / 2
        self.logoPosY = -LoadSprite("logo").get_height() / 2
        self.buttonTime = 0
        self.buttonSpeed = 0.25
        self.speed = 100