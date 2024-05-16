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

    def draw(self, deltaTime: float, time: float):
        
        self.frameTimer += deltaTime

        if self.frameTimer > 1/20:
            self.frameTimer = 0
            self.frame += 1

        DrawSprite( "Explosion/" + str(self.frame), self.posX, self.posY)
        print("Drawing explosion at",self.posX, self.posY)

        pass