from Input import Input
import pygame as pg
from SpriteRegistry import *


class Explosion:

    posX = 0
    posY = 0

    frameTimer = 0

    frame = 0

    FPS = 10

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, screen: pg.surface.Surface, deltaTime: float, time: float):
        
        self.frameTimer += deltaTime

        if self.frameTimer > 1/20:
            self.frameTimer = 0
            self.frame += 1

        DrawSprite(screen, "Explosion/" + str(self.frame), self.posY, self.posX)
        print("Drawing explosion at",self.posX, self.posY)

        pass