from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window


class EnemyBullet:

    posX = 0
    posY = 0
    speedX = 0
    speedY = 200

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):
        
        if self.posY > Window.WINDOW._actualHeight and self in Window.WINDOW._game._enemyBullets:
            Window.WINDOW._game._enemyBullets.remove(self)
        if self.posY < 0 and self in Window.WINDOW._game._enemyBullets:
            Window.WINDOW._game._enemyBullets.remove(self)
        if self.posX > Window.WINDOW._actualWidth and self in Window.WINDOW._game._enemyBullets:
            Window.WINDOW._game._enemyBullets.remove(self)
        if self.posX < 0 and self in Window.WINDOW._game._enemyBullets:
            Window.WINDOW._game._enemyBullets.remove(self)

        self.posY += deltaTime * self.speedY
        self.posX += deltaTime * self.speedX

        DrawSprite("bullet", self.posX + 7, self.posY)

        pass