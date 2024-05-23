from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
import math



class Bullet:

    posX = 0
    posY = 0

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):
        
        if self.posY < 0 and self in Window.WINDOW._game._bullets:
            Window.WINDOW._game._bullets.remove(self)

        self.posY -= deltaTime * 240 * 2

        DrawSprite("bullet", self.posX-1, self.posY)

        pass