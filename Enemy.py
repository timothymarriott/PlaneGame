from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from EnemyBullet import EnemyBullet


class Enemy:
    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, screen: pg.surface.Surface, deltaTime: float, time: float):

        self.posY += deltaTime * 60

        DrawSprite(screen, "defaultEnemy", self.posX, self.posY)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)

        if self.distanceToPlayer < 10:
            Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY))
        
        pass