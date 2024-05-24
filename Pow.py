from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt


class Pow:

    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):

        DrawSprite("Powerup", self.posX-1, self.posY)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)

        self.posY += 25 * deltaTime

        if self.distanceToPlayer < 25:
            print("Spaghetti")
            Window.WINDOW._game._pow = True
            Window.WINDOW._game._powTime = 0
        
            if self in Window.WINDOW._game._powerUps:
                Window.WINDOW._game._powerUps.remove(self)
                
                
        if self.posY > Window.WINDOW._actualHeight:
            if self in Window.WINDOW._game._powerUps:
                Window.WINDOW._game._powerUps.remove(self)


        pass