from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from EnemyBullet import EnemyBullet
from Explosion import  Explosion

class CollisionEnemy:
    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100
    enemyAliveTimer = 0

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):

        self.enemyAliveTimer += deltaTime

        self.posY += deltaTime * 300

        DrawSprite("collideEnemy", self.posX, self.posY)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)

        if self.enemyAliveTimer  > 5:
            if self.posY > Window.WINDOW._actualHeight and self in Window.WINDOW._game._enemies :
                Window.WINDOW._game._enemies.remove(self)

           
            if self.posY < 10 and self in Window.WINDOW._game._enemies:
                Window.WINDOW._game._enemies.remove(self)

        if self.distanceToPlayer < 30:
            if Window.WINDOW._game._player.doRender != False:
                Window.WINDOW._game._player.doRender = False
                Window.WINDOW._game._explosions.append(Explosion(Window.WINDOW._game._player.posX, Window.WINDOW._game._player.posY))
                Window.WINDOW._game._explosions.append(Explosion(self.posX, self.posY))
                Window.WINDOW._game._collisionEnemies.remove(self)

        pass