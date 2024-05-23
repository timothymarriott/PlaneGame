from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from EnemyBullet import EnemyBullet
from Explosion import  Explosion
from random import random as rand
import math

class Boss:
    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100

    health = 50 #amount of times u need to shoot the boss before death

    shootTimer = 0
    timeUntilShot = 4
    nextBossAttack = 0
    amountOfAttacks = 2
    choseStuff = False

    minTimeUntilShot = 6
    maxTimeUntilShot = 12

    #next boss attack is the next type of attack the boss will do
    #0 is the average shot and 1  is a big boom, shooting bullets in every direction.

    def __init__(self, x: int, y: int) -> None:
        Window.WINDOW._game._spawnWaves = False
        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):

        if self.posY < 30:
            self.posY += 25 * deltaTime

        
        DrawSprite("boss", self.posX, self.posY)

        self.shootTimer += deltaTime

        if self.health <= 0:
            print("boss dead")
            Window.WINDOW._game._boss = None

        if self.shootTimer >= self.timeUntilShot:
            if self.nextBossAttack == 0:
                yOffsetDown = 60
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 10, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 20, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 30, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 40, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 50, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 100, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 110, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 120, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 130, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 140, self.posY + yOffsetDown))
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 150, self.posY + yOffsetDown))
            if self.nextBossAttack == 1:
                print("supposed to spawn circle attack")
            self.shootTimer = 0
            self.timeUntilShot = round(rand()) * (self.maxTimeUntilShot - self.minTimeUntilShot) + self.minTimeUntilShot
            self.nextBossAttack = math.ceil(rand() * self.amountOfAttacks -  1)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)


        if self.distanceToPlayerX < 160 and self.distanceToPlayerY < 200:
            #boss collider
            if Window.WINDOW._game._player.doRender != False and not Window.WINDOW._game._player._godmode:
                Window.WINDOW._game._player.doRender = False
                Window.WINDOW._game._explosions.append(Explosion(Window.WINDOW._game._player.posX, Window.WINDOW._game._player.posY))

        pass