from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from EnemyBullet import EnemyBullet
from Explosion import  Explosion
from random import random as rand
import Game as Game
import math
from SoundRegistry import *

class Boss:
    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100

    health = 50 #amount of times u need to shoot the boss before death

    moveDir = 1
    moveSpeed = 30
    
    bossSprite = 0

    shootTimer = 0
    timeUntilShot = 4
    nextBossAttack = 0
    amountOfAttacks = 2
    choseStuff = False

    bossAliveTimer = 0

    minTimeUntilShot = 3
    maxTimeUntilShot = 4.5

    circleShootSize = 10

    deadTimer = 0
    bossDead = False
    explosionAnim = 0

    sideBufferSpace = 0

    #next boss attack is the next type of attack the boss will do
    #0 is the average shot and 1  is a big boom, shooting bullets in every direction.

    def __init__(self, x: int, y: int, _health: int, circleAmt: int) -> None:
        Window.WINDOW._game._spawnWaves = False

        self.bossSprite = 0

        if Window.WINDOW._game._bossesSpawned > 1:
            if rand() * 100 <= 1: 
                self.bossSprite = 1

        self.circleShootSize = circleAmt

        self.explosionAnim = 0
        self.bossDead = False
        self.posX = x
        self.posY = y
        self.health = _health
        self.sideBufferSpace = LoadSprite("boss").get_width()
        pass

    def draw(self, deltaTime: float, time: float):

        if self.posY < 30:
            self.posY += 25 * deltaTime
        
        if self.bossSprite == 0:
            DrawSprite("boss", self.posX, self.posY)
        if self.bossSprite == 1:
            DrawSprite("ShockedSeb", self.posX, self.posY)
            if self.shootTimer > 5:
                Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX + 75, self.posY + 80))

        self.bossAliveTimer += deltaTime

        self.shootTimer += deltaTime

        if self.health <= 0:
            self.bossDead = True
            self.deadTimer += deltaTime
            yOffsetDown = 60


            if self.deadTimer > 0.2 and self.explosionAnim == 0:
                self.explosionAnim += 1
                Window.WINDOW._game._explosions.append(Explosion(self.posX, self.posY + yOffsetDown))
            if self.deadTimer > 0.3 and self.explosionAnim == 1:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 10, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 0.5 and self.explosionAnim == 2:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 20, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 0.6 and self.explosionAnim == 3:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 30, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 0.7 and self.explosionAnim == 4:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 40, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 0.8 and self.explosionAnim == 5:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 50, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.2 and self.explosionAnim == 6:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 100, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.3 and self.explosionAnim == 7:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 110, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.4 and self.explosionAnim == 8:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 120,  self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.5 and self.explosionAnim == 9:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 130, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.6 and self.explosionAnim == 10:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 140, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.deadTimer > 1.7 and self.explosionAnim == 11:
                Window.WINDOW._game._explosions.append(Explosion(self.posX + 150, self.posY + yOffsetDown))
                self.explosionAnim += 1
            if self.explosionAnim == 12:
                Window.WINDOW._game._boss = None
                Window.WINDOW._game._spawnWaves = True
                PlaySound("B_Die")

        if self.shootTimer >= self.timeUntilShot:
            yOffsetDown = 60
            if self.nextBossAttack == 0:
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
                Game.MakeBulletCircle(self.posX + 75, self.posY + yOffsetDown, self.circleShootSize)
            self.shootTimer = 0
            self.timeUntilShot = round(rand()) * (self.maxTimeUntilShot - self.minTimeUntilShot) + self.minTimeUntilShot
            self.nextBossAttack = math.ceil(rand() * self.amountOfAttacks -  1)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)

        if self.bossAliveTimer > 5:
            self.posX += self.moveSpeed * self.moveDir * deltaTime / 2

            if self.posX < 0:
                self.posX = 0
                self.moveDir = 1
            if self.posX > Window.WINDOW._actualWidth - self.sideBufferSpace:
                self.posX = Window.WINDOW._actualWidth - self.sideBufferSpace
                self.moveDir = -1

        '''
        if self.move == True:

            #if move spot is 0, go to center, move spot is 1, go to right, move spot 2, go right.
            if self.setMovement == False:
                self.moveDir = round(rand() * 3)
                self.setMovement = True
                
                if self.moveDir < 1 and self.moveDir > 0:
                    if not self.posX + 80 < 150:
                        self.moveDir = 15
                        self.moveSpot = 2
                    else:
                        self.moveDir = 1.5
                if self.moveDir <= 3 and self.moveDir > 2:
                    if not self.posX + 80 > 80:
                        self.moveDir = -15
                        self.moveSpot = 1
                    else:
                        self.moveDir = 1.5
                if self.moveDir < 2 and self.moveDir > 1:
                    if self.posX + 80 < 110:
                        self.moveDir = 15
                    if self.posX + 80  >= 115:
                        self.moveDir = -15
                        self.moveSpot = 0
            
            if self.moveSpot == 0:
                if self.posX + 80 > 120 and self.posX + 80 < 125:
                    self.setMovement = False
                else:
                    self.posX += self.moveDir * deltaTime
            if self.moveSpot == 2:
                if self.posX + 80 > 150:
                    self.setMovement = False
                else:
                     self.posX += self.moveDir * deltaTime
            if self.moveSpot == 1:
                if self.posX + 80 < 100:
                    self.setMovement = False
                else:
                    self.posX += self.moveDir * deltaTime
                    
        '''


        if self.distanceToPlayerX < 160 and self.distanceToPlayerY < 100:
            #boss collider
            if Window.WINDOW._game._player.doRender != False and not Window.WINDOW._game._player._godmode:
                Window.WINDOW._game._player.doRender = False
                Window.WINDOW._game._explosions.append(Explosion(Window.WINDOW._game._player.posX, Window.WINDOW._game._player.posY))

        pass