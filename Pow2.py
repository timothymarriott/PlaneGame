from Input import Input
import pygame as pg
from SpriteRegistry import *
import Window
from math import sqrt
from Bullet import Bullet


class Pow2:

    posX = 0
    posY = 0
    distanceToPlayerX = 100
    distanceToPlayerY = 100
    distanceToPlayer = 100

    def __init__(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y
        pass

    def usePowerup():
        Window.WINDOW._game._bullets.append(Bullet(0, 293))
        Window.WINDOW._game._bullets.append(Bullet(10, 293))
        Window.WINDOW._game._bullets.append(Bullet(20, 293))
        Window.WINDOW._game._bullets.append(Bullet(30, 293))
        Window.WINDOW._game._bullets.append(Bullet(40, 293))
        Window.WINDOW._game._bullets.append(Bullet(50, 293))
        Window.WINDOW._game._bullets.append(Bullet(60, 293))
        Window.WINDOW._game._bullets.append(Bullet(70, 293))
        Window.WINDOW._game._bullets.append(Bullet(80, 293))
        Window.WINDOW._game._bullets.append(Bullet(90, 293))
        Window.WINDOW._game._bullets.append(Bullet(100, 293))
        Window.WINDOW._game._bullets.append(Bullet(110, 293))
        Window.WINDOW._game._bullets.append(Bullet(120, 293))
        Window.WINDOW._game._bullets.append(Bullet(130, 293))
        Window.WINDOW._game._bullets.append(Bullet(140, 293))
        Window.WINDOW._game._bullets.append(Bullet(150, 293))
        Window.WINDOW._game._bullets.append(Bullet(160, 293))
        Window.WINDOW._game._bullets.append(Bullet(170, 293))
        Window.WINDOW._game._bullets.append(Bullet(180, 293))
        Window.WINDOW._game._bullets.append(Bullet(190, 293))
        Window.WINDOW._game._bullets.append(Bullet(200, 293))
        Window.WINDOW._game._bullets.append(Bullet(210, 293))
        Window.WINDOW._game._bullets.append(Bullet(220, 293))

    def renderPower():
        if Window.WINDOW._game._pow2Num >= 1:
            DrawSprite("Pow2Vis", 237, 199)
        if Window.WINDOW._game._pow2Num >= 2:
            DrawSprite("Pow2Vis",20, 213)
        if Window.WINDOW._game._pow2Num == 3:
            DrawSprite("Pow2Vis", 30, 213)    


    def draw(self, deltaTime: float, time: float):

        DrawSprite("Powerup2", self.posX-1, self.posY)

        self.distanceToPlayerX = abs(Window.WINDOW._game._player.posX - self.posX)
        self.distanceToPlayerY = abs(Window.WINDOW._game._player.posY - self.posY)
        self.distanceToPlayer = sqrt(self.distanceToPlayerX * self.distanceToPlayerX + self.distanceToPlayerY * self.distanceToPlayerY)

        self.posY += 25 * deltaTime

        if self.distanceToPlayer < 25:
            print("Spaghettwo")
        
            if self in Window.WINDOW._game._powerUps2:
                Window.WINDOW._game._powerUps2.remove(self)
            
            if Window.WINDOW._game._pow2Num < 3:
                Window.WINDOW._game._pow2Num += 1
                print(str(Window.WINDOW._game._pow2Num))
        
            
                
        if self.posY > Window.WINDOW._actualHeight:
            if self in Window.WINDOW._game._powerUps2:
                Window.WINDOW._game._powerUps2.remove(self)


        pass