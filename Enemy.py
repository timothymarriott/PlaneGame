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
    hasShot = False
    shootTimer = 0
    movementTimer = 0

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):


        if self.hasShot == True:
            self.movementTimer += deltaTime

        if self.movementTimer == 0:
            self.posY += deltaTime * 60
        elif self.movementTimer > 1:
            self.posY += deltaTime * -100
        elif  self.movementTimer > 0.6:
            self.posY += deltaTime * -50
        elif self.movementTimer  > 0.25:
            self.posY += deltaTime * -20
        self.shootTimer += deltaTime

        DrawSprite("defaultEnemy", self.posX, self.posY)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)
   
        if self.distanceToPlayer < 100:
            if self.posY < Window.WINDOW._game._player.posY:
                if Window.WINDOW._game._player.doRender == True:
                    if self.distanceToPlayerX < 15:
                        if self.shootTimer > 1:
                            Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY))
                            self.shootTimer = 0
                            self.hasShot = True
                    if Window.WINDOW._game._player.posX - self.posX < -15:
                        if self.shootTimer > 1:
                            Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY))
                            enemyB = Window.WINDOW._game._enemyBullets[len(Window.WINDOW._game._enemyBullets) - 1]
                            enemyB.speed /= 2
                            enemyB.rot = -45
                            self.shootTimer = 0
                            self.hasShot = True
                    if self.distanceToPlayerX > 15:
                        if self.shootTimer > 1:
                            Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY))
                            enemyB = Window.WINDOW._game._enemyBullets[len(Window.WINDOW._game._enemyBullets) - 1]
                            enemyB.rot = 45
                            enemyB.speed /= 2
                            self.hasShot= True
                            self.shootTimer = 0
        
        pass