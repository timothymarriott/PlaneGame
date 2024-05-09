from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window


class Bullet:

    posX = 0
    posY = 0


    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, screen: pg.surface.Surface, deltaTime: float, time: float):
        
        if self.posY < 0:
            Window.WINDOW._game._bullets.remove(self)

        self.posY -= deltaTime * 240 * 2

        DrawSprite(screen, "bullet", self.posX-1, self.posY)
        print("Drawing Bullet at",self.posX-1, self.posY)

        pass