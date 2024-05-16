from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window

class Player:

    posX = 0
    posY = 0

    PlaneType = "green"

    _speed = 130

    def __init__(self) -> None:
        RegisterSprite(self.PlaneType, "Planes/" + self.PlaneType + ".png")
        pass

    def draw(self, deltaTime: float, time: float):
        if Input.GetKey(pg.K_a):
            self.posX -= self._speed * deltaTime
        if Input.GetKey(pg.K_d):
            self.posX += self._speed * deltaTime
            
        if Input.GetKey(pg.K_w):
            self.posY -= self._speed * deltaTime
        if Input.GetKey(pg.K_s):
            self.posY += self._speed * deltaTime
            

        if (self.posX < 13):
            self.posX = 13
        if (self.posY < 100):
            self.posY = 100

        if (self.posY > Window.WINDOW._actualHeight - 40):
            self.posY = Window.WINDOW._actualHeight - 40

        if (self.posX > Window.WINDOW._actualWidth - 13):
            self.posX = Window.WINDOW._actualWidth - 13

        DrawSprite(self.PlaneType, self.posX-LoadSprite(self.PlaneType).get_width()/2, self.posY-LoadSprite(self.PlaneType).get_height()/2)
        pass