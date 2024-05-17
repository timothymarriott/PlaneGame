from Input import Input
import pygame as pg
from SpriteRegistry import *
from Background import Background
from Explosion import Explosion
from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from CollisionEnemy import CollisionEnemy
from EnemyBullet import EnemyBullet
from random import random as rand
from Menu import Menu
from Text import *
from math import floor


class Game:

    _background: Background = None
    _explosions = []
    _bullets = []
    _enemies = []
    _enemyBullets = []
    _collisionEnemies = []

    _player: Player = None

    _cooldown: float = 0
    _shotcount: int = 0

    _menu: Menu

    _SkipMenu: bool = False

    _waveTime: float = 2

    _showDebug: bool = False

    _score: int = 0

    _minEnemiesPerWave = 3
    _maxEnemiesPerWave = 5
    
    _wave = 0

    def __init__(self) -> None:
        global GAME
        GAME = self
        pass
        

    def Start(self):
        self._background = Background()
        self._player = Player()
        self._menu = Menu()
        self._menu.Start()
        RegisterSprite("Explosion/0", "Explosion/frame1.png")
        RegisterSprite("Explosion/1", "Explosion/frame2.png")
        RegisterSprite("Explosion/2", "Explosion/frame3.png")
        RegisterSprite("Explosion/3", "Explosion/frame4.png")
        RegisterSprite("Explosion/4", "Explosion/frame5.png")
        RegisterSprite("Explosion/5", "Explosion/frame6.png")
        RegisterSprite("bullet", "Bullet.png")
        RegisterSprite("defaultEnemy", "smallGreenPlane.png")
        RegisterSprite("collideEnemy", "FatGreyPlane.png")
        LoadChars()
        pg.mixer.music.load("./Assets/music_main.mp3")
        pg.mixer.music.play(-1)
        pass

    def Update(self, deltaTime: float, time: float):
        
            

        if not self._SkipMenu:
            self._menu.Draw()
            return
        
        if Input.GetKeyDown(pg.K_ESCAPE):
            self._menu.Reset()
            self._SkipMenu = False

        if Input.GetKeyDown(pg.K_z):
            self._showDebug = not self._showDebug
        if Input.GetKeyDown(pg.K_i):
            self._player._godmode = not self._player._godmode


        self._background.draw(deltaTime, time)
        

        mousePos = pg.mouse.get_pos()

        if self._waveTime <= 0:
            for i in range(round(rand()) * (self._maxEnemiesPerWave - self._minEnemiesPerWave) + self._minEnemiesPerWave):
                if round(rand() * 10) == 1 and self._wave > 3:
                    self._collisionEnemies.append(CollisionEnemy(rand() * 200, rand() * -100))
                else:
                    self._enemies.append(Enemy(rand() * 200, rand() * -100))
            self._wave += 1
            self._waveTime = 8
            for i in range(self._wave):
                self._waveTime *= 0.9
            
            #Wave = WAVES[round(rand()*(len(WAVES) - 1))]
            #print(Wave)
            #for plane in Wave:
            #    self._enemies.append(Enemy(Window.WINDOW._actualWidth / 2 + plane[0] * 75, plane[1] * 75 - 100))

        

        self._waveTime -= deltaTime

        if Input.GetKeyDown(pg.K_SPACE):
            if self._player.doRender == True:
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
            else:
                explosion.draw(deltaTime, time)

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
                        self._score += 10
                        break
            for enemy in self._collisionEnemies:
                enemy : CollisionEnemy
                colSize = 25
                if abs(enemy.posX + colSize / 1.25 - bullet.posX) < colSize and abs(bullet.posX - enemy.posX) < colSize:
                    if abs(enemy.posY + colSize / 1.25 - bullet.posY) < colSize and abs(bullet.posY - enemy.posY) < colSize:
                        self._explosions.append(Explosion(enemy.posX, enemy.posY))
                        self._collisionEnemies.remove(enemy)
                        self._bullets.remove(bullet)
                        self._score += 10
                        break


            bullet.draw(deltaTime, time)
            

        for enemyBullet in self._enemyBullets:
            enemyBullet: EnemyBullet

            colSize = 22
            if abs(self._player.posX - enemyBullet.posX) < colSize and abs(enemyBullet.posX + colSize / 1.25 - self._player.posX) < colSize:
                if abs(self._player.posY - enemyBullet.posY) < colSize and abs(enemyBullet.posY + colSize / 1.25 - self._player.posY) < colSize:
                    if self._player.doRender and not self._player._godmode:
                        
                        print("player died :sob:")
                        self._explosions.append(Explosion(self._player.posX - 10, self._player.posY - 5))
                        self._enemyBullets.remove(enemyBullet)
                        self._player.doRender = False


            enemyBullet.draw( deltaTime, time)

        for enemy in self._enemies:
            enemy: Enemy
            enemy.draw(deltaTime, time)
            
        for collisionEnemy in self._collisionEnemies:
            collisionEnemy : CollisionEnemy 
            collisionEnemy.draw(deltaTime, time)

        self._player.draw( deltaTime, time)
        
        y = 0
        

        if self._showDebug:
            DrawText("SCORE: " + str(self._score), 0, y, (255, 255, 255))
            y += GetTextHeight("SCORE: " + str(self._score))
            DrawText("WAVE TIME: " + str(round(self._waveTime, 2)), 0, y, (255, 255, 255))
            y +=  + GetTextHeight("WAVE TIME: " + str(round(self._waveTime, 2)))
            DrawText("X: " + str(floor(self._player.posX)), 0, y, (255, 255, 255))
            DrawText("Y: " + str(floor(self._player.posY)), 0 + GetTextWidth("X: 999"), y, (255, 255, 255))
            y += GetTextHeight("X: " + str(floor(self._player.posX)) + "Y: " + str(floor(self._player.posY)))
            DrawText("ENEMY COUNT: " + str(len(self._enemies)), 0, y, (255, 255, 255))
            y += GetTextHeight("ENEMY COUNT: " + str(len(self._enemies)))
            DrawText("GOD MODE: " + str(self._player._godmode), 0, y, (255, 255, 255))
            y += GetTextHeight("GOD MODE: " + str(self._player._godmode))
            DrawText("WAVE: " + str(self._wave), 0, y, (255, 255, 255))
            y += GetTextHeight("WAVE: " + str(self._wave))

            totalWaveTime = 8
            for i in range(self._wave):
                totalWaveTime *= 0.9

            DrawText("TOTAL WAVE TIME: " + str(round(totalWaveTime, 2)), 0, y, (255, 255, 255))
            y +=  + GetTextHeight("TOTAL WAVE TIME: " + str(round(totalWaveTime, 2)))

        
        return
    
