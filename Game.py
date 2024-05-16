from Input import Input
import pygame as pg
from SpriteRegistry import *
from Background import Background
from Explosion import Explosion
from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from EnemyBullet import EnemyBullet
from random import random as rand
from Menu import Menu

class Game:

    _background: Background = None
    _explosions = []
    _bullets = []
    _enemies = []
    _enemyBullets = []

    _player: Player = None

    _cooldown: float = 0
    _shotcount: int = 0

    _menu: Menu

    

    def __init__(self) -> None:
        global GAME
        GAME = self
        pass
        

    def Start(self):
        self._background = Background()
        self._player = Player()
        self._menu = Menu()
        RegisterSprite("Explosion/0", "Explosion/frame1.png")
        RegisterSprite("Explosion/1", "Explosion/frame2.png")
        RegisterSprite("Explosion/2", "Explosion/frame3.png")
        RegisterSprite("Explosion/3", "Explosion/frame4.png")
        RegisterSprite("Explosion/4", "Explosion/frame5.png")
        RegisterSprite("Explosion/5", "Explosion/frame6.png")
        RegisterSprite("bullet", "Bullet.png")
        RegisterSprite("defaultEnemy", "smallGreenPlane.png")
        pass

    def Update(self, deltaTime: float, time: float):
        

        self._background.draw(deltaTime, time)

        mousePos = pg.mouse.get_pos()

        if Input.GetKeyDown(pg.K_e):
            self._explosions.append(Explosion(mousePos[1] / 2, mousePos[0] / 2))

        if Input.GetKeyDown(pg.K_f):
            
            self._enemies.append(Enemy(rand() * 200, 0))

        if Input.GetKeyDown(pg.K_SPACE):
            if self._cooldown <= 0:
                if self._shotcount >= 3:
                    self._cooldown = 0.2
                    self._shotcount = 0
                self._shotcount += 1
                self._bullets.append(Bullet(self._player.posX - 5, self._player.posY))
                self._bullets.append(Bullet(self._player.posX + 5, self._player.posY))

        self._cooldown -= deltaTime

        for explosion in self._explosions:
            explosion: Explosion
            if explosion.frame > 4:
                self._explosions.remove(explosion)
                print("Killed Explosion")
            else:
                explosion.draw(deltaTime, time)
                print("Drawing Explosion")

        for bullet in self._bullets:
            bullet: Bullet


            for enemy in self._enemies:
                enemy: Enemy
                colSize = 18
                if abs(enemy.posX + colSize / 1.25 - bullet.posX) < colSize and abs(bullet.posX - enemy.posX) < colSize:
                    if abs(enemy.posY + colSize / 1.25 - bullet.posY) < colSize and abs(bullet.posY - enemy.posY) < colSize:
                        self._explosions.append(Explosion(enemy.posX, enemy.posY))
                        self._enemies.remove(enemy)
                        self._bullets.remove(bullet)


            bullet.draw(deltaTime, time)
            

        for enemyBullet in self._enemyBullets:
            enemyBullet : EnemyBullet
            enemyBullet.draw( deltaTime, time)

        for enemy in self._enemies:
            enemy: Enemy
            enemy.draw(deltaTime, time)
            

        self._player.draw( deltaTime, time)
        
        return
    
