from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window


class Enemy:
    posX = 0
    posY = 0

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, screen: pg.surface.Surface, deltaTime: float, time: float):

        self.posY += deltaTime * 60

        DrawSprite(screen, "defaultEnemy", self.posX, self.posY)

        pass