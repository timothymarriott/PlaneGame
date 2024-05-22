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
from Program import app_folder
import os
import Leaderboard

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

    #Improved wave spawning variables. Controls alot about the wave spawning.
    _startWaveTime: int = 7
    _scaling: float = 115
    _timeBetweenWaves: float = _startWaveTime
    _stopScalingAt: float = 1.5


    _colEnemyChance: float = 1 #When rolling one in 10, checks if it is equal to or smaller than this number. Increase to change spawn odds.
    _maxColChance: int = 3


    _wavesBetweenCountUp: float = 10
    _wavesSinceLastCount: int = 0

    _score: int = 0
    _highScore: int = 0
    _lastHighscore: int = 0

    _minEnemiesPerWave = 3
    _maxEnemiesPerWave = 5
    
    _wave = 0

    _Muted: bool = False

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

        config = os.path.join(app_folder("1942-Remake"), "settings.ini")
        print(app_folder("1942-Remake"))
        if os.path.exists(config):
        
            configFile = open(config, "+r")
            lines = configFile.readlines()
            if "Muted = 1" in lines[1]:
                self._Muted = True
            elif "Muted = 1" in lines[1]:
                self._Muted = False
            
            self._highScore = int(lines[4].replace("HighScore = ", ""))


            configFile.close()
        
        pass

    def Update(self, deltaTime: float, time: float):
        
        if self._Muted:
            pg.mixer.music.set_volume(0)
        else:
            pg.mixer.music.set_volume(1)

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
                if round(rand() * 10) <= self._colEnemyChance and self._wave > 3:
                    self._collisionEnemies.append(CollisionEnemy(rand() * 200, rand() * -100))
                else:
                    self._enemies.append(Enemy(rand() * 200, rand() * -100))
            self._wave += 1
            self._waveTime = self._startWaveTime
            for i in range(self._wave):
                if self._timeBetweenWaves > self._stopScalingAt:
                    self._waveTime *= 1 - (self._waveTime) / self._scaling
                else:
                    self._waveTime = self._stopScalingAt
            self._timeBetweenWaves = self._waveTime
            self._wavesSinceLastCount += 1

            if self._wavesSinceLastCount >= self._wavesBetweenCountUp:
                self._maxEnemiesPerWave += 1
                self._minEnemiesPerWave += 1
                self._wavesBetweenCountUp *= 1.5
                self._wavesSinceLastCount = 0

            if self._colEnemyChance < self._maxColChance:
                self._colEnemyChance = self._wave / 10
            else:
                self._colEnemyChance = self._maxColChance

            
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
                        if self._score > self._lastHighscore:
                            Leaderboard.UploadScore(Window.WINDOW._game._score)


            enemyBullet.draw( deltaTime, time)

        for enemy in self._enemies:
            enemy: Enemy
            enemy.draw(deltaTime, time)
            
        for collisionEnemy in self._collisionEnemies:
            collisionEnemy : CollisionEnemy 
            collisionEnemy.draw(deltaTime, time)

        self._player.draw( deltaTime, time)
        
        if self._score > self._highScore:
            self._highScore = self._score
        
        y = 0
        

        if self._showDebug:
            DrawText("SCORE: " + str(self._score), 0, y, (255, 255, 255))
            y += GetTextHeight("SCORE: " + str(self._score))
            DrawText("HIGH SCORE: " + str(self._highScore), 0, y, (255, 255, 255))
            y += GetTextHeight("HIGH SCORE: " + str(self._highScore))
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

            totalWaveTime = self._timeBetweenWaves

            DrawText("TOTAL WAVE TIME: " + str(round(totalWaveTime, 2)), 0, y, (255, 255, 255))
            y +=  + GetTextHeight("TOTAL WAVE TIME: " + str(round(totalWaveTime, 2)))

        
        return
    
    def End(self):
        
        config = os.path.join(app_folder("1942-Remake"), "settings.ini")
        if os.path.exists(config):
            os.remove(config)
        
        configFile = open(config, "+w")
        if self._Muted:
            configFile.write("[Audio]\nMuted = 1\n")
        else:
            configFile.write("[Audio]\nMuted = 0\n")

        configFile.write("\n[Scores]\nHighScore = " + str(self._highScore))

        configFile.close()
        pass
    
