from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from EnemyBullet import EnemyBullet
from Explosion import  Explosion
from random import random as rand
from Player import Player

class Enemy:
    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100
    hasShot = False
    shootTimer = 0
    movementTimer = 0
    enemyAliveTimer = 0

    bombEnemyChance = 2 #10 = 100% chance 1 = 10% chance.
    bomberEnemy = False
    bomberAttackRange = 100
    bombDirection: int = 0
    checkedBombDir: bool = False
    startedBombing: bool = False
    hasCheckedIfBomber: bool = False # im sorry for all the variables btw just for organisation.

    bulletShootDistance = 125

    def __init__(self, x: int, y: int) -> None:

        self.posX = x
        self.posY = y
        pass

    def draw(self, deltaTime: float, time: float):

        if self.hasCheckedIfBomber == False:
            if round(rand() * 10) <= self.bombEnemyChance:
                self.bomberEnemy = True
                self.bulletShootDistance = 0

        self.hasCheckedIfBomber = True
        
        self.enemyAliveTimer += deltaTime

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

        #note to self, bigger y = further down, not further up.
        #another note to self, lower x = further to left, higher x = further to right.
        if self.bomberEnemy == True:
            if self.distanceToPlayer < self.bomberAttackRange and self.posY + 10 < Window.WINDOW._game._player.posY:

                #bomb direction determines if the bomber knows where hes going. 
                # the bomb direction will change depending on which direction, and how far in said direction the player is.
                # if bomb direction is 10, he will move 10 pixels to the right every frame.
                # if it is 0, it has not been set yet.

                if self.checkedBombDir == False:
                    
                    self.checkedBombDir = True
                    if self.distanceToPlayer < 15:
                        # enemy is "straight above" the player.
                        self.bombDirection = 0
                    elif Window.WINDOW._game._player.posX - self.posX > 0:
                        # enemy to left of player
                        self.bombDirection = Window.WINDOW._game._player.posX - self.posX
                    elif Window.WINDOW._game._player.posX - self.posX < 0:
                        #enemy to right of player
                        self.bombDirection = Window.WINDOW._game._player.posX - self.posX


            if self.checkedBombDir == True:
                self.posY += 15 * deltaTime
                self.posX += self.bombDirection * deltaTime
        
        if self.distanceToPlayer < self.bulletShootDistance:
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
                            enemyB.speedY /= 1.5
                            
                            enemyB.speedX = -100
                            
                            self.shootTimer = 0
                            self.hasShot = True
                    if self.distanceToPlayerX > 15:
                        if self.shootTimer > 1:
                            Window.WINDOW._game._enemyBullets.append(EnemyBullet(self.posX, self.posY))
                            enemyB = Window.WINDOW._game._enemyBullets[len(Window.WINDOW._game._enemyBullets) - 1]
                            
                            enemyB.speedY /= 1.5
                            enemyB.speedX = 100

                            self.hasShot= True
                            self.shootTimer = 0
        
        if self.enemyAliveTimer  > 5:
            if self.posY > Window.WINDOW._actualHeight and self in Window.WINDOW._game._enemies :
                Window.WINDOW._game._enemies.remove(self)

           
            if self.posY < 10 and self in Window.WINDOW._game._enemies:
                Window.WINDOW._game._enemies.remove(self)

        if self.distanceToPlayer < 20:
            if not Window.WINDOW._game._player._godmode:
                if Window.WINDOW._game._player.doRender != False:
                    Window.WINDOW._game._player.doRender = False
                    Window.WINDOW._game._explosions.append(Explosion(Window.WINDOW._game._player.posX, Window.WINDOW._game._player.posY))
                    Window.WINDOW._game._explosions.append(Explosion(self.posX, self.posY))
                    Window.WINDOW._game._enemies.remove(self)

        pass