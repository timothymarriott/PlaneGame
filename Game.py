from Input import Input
import pygame as pg
from SpriteRegistry import *
from SoundRegistry import *
from Background import Background
from Explosion import Explosion
from Player import Player
from Bullet import Bullet
from Enemy import Enemy
from CollisionEnemy import CollisionEnemy
from EnemyBullet import EnemyBullet
from random import random as rand
from Menu import Menu
from Boss import Boss
from Text import *
from math import floor
from Program import app_folder
from Pow import Pow
from Pow2 import Pow2
from math import sqrt
import os
import math


def generate_circle_points(radius, num_points):
    """
    Generates a set of points evenly spaced on a circle.

    :param radius: The radius of the circle.
    :param num_points: The number of points to generate.
    :return: A list of tuples representing the points on the circle.
    """

    startPos = round(rand() * 100)

    points = []
    angle_increment = 2 * math.pi / num_points
    
    for i in range(num_points):
        angle = i + startPos * angle_increment
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((x, y))
    
    return points

def MakeBulletCircle(x: int, y: int, amount: int):
    bulletDirs = generate_circle_points(1, amount)
    for dir in bulletDirs:
        bullet = EnemyBullet(x, y)
        bullet.speedX = dir[0] * 200
        bullet.speedY = dir[1] * 200
        Window.WINDOW._game._enemyBullets.append(bullet)
    pass


class Game:

    _background: Background = None

    _explosions = []
    _bullets = []
    _enemies = []
    _enemyBullets = []
    _collisionEnemies = []
    _boss = None
    _powerUps = []
    _powerUps2 = []
    _powerUps2Vis = []

    _bossSpawnIncrease: int = 0
    _startBossHealth: int = 120
    _nextBossHealth: int = _startBossHealth

    _player: Player = None

    _cooldown: float = 0
    _shotcount: int = 0

    _menu: Menu

    _SkipMenu: bool = False

    _waveTime: float = 2

    _showDebug: bool = False

    #Improved wave spawning variables. Controls alot about the wave spawning.
    _startWaveTime: int = 7 #How fast the waves are at the start of the game.
    
    _scaling: float = 115 #Dont worry about this, higher number will make the waves times decrease slower.

    _timeBetweenWaves: float = _startWaveTime

    _stopScalingAt: float = 1.5 #This is the FASTEST waves can spawn. Increase/decrease to change.

    _spawnWaves: bool = True
    _decreaseWaveTime: bool = True


    _colEnemyChance: float = 1 #When rolling one in 10 to choose enemy, checks if it is equal to or smaller than this number. Increase to change spawn odds.
    _maxColChance: int = 3 #The max percentage change of a collision enemy (chance = var * 10, so if its 3, theres a 30% chance.)


    _wavesBetweenCountUp: float = 10 #Controls the waves (for  the first time) until there is a new enemy per wave.
    _wavesSinceLastCount: int = 0 #Controls how many waves have gone  past since it has made more enemies spawn.

    _score: int = 0
    _highScore: int = 0
    _lastHighscore: int = 0

    _minEnemiesPerWave = 3
    _maxEnemiesPerWave = 5
    
    _wave = 0

    _Muted: bool = False

    _pow: bool = False
    _pow2: bool = False
    _powTime: float = 0
    _pow2Num: int = 0

    _EnteredGodMode = False

    _bossesSpawned: int = 0

    _debugY: int = 0
    def DrawDebugText(self, text: str, color = (255, 255, 255)) -> None:
        DrawText(text, 0, self._debugY, color)
        self._debugY += GetTextHeight(text)

    def __init__(self) -> None:
        global GAME
        GAME = self
        pass
        

    def Start(self):

        
        self._background = Background()
        self._player = Player()
        self._menu = Menu()
        self._menu.Start()
        RegisterSound("Explode", "Explode.mp3")
        RegisterSound("B_Die", "BossDie.mp3")
        RegisterSound("Shot", "Shot.mp3")
        RegisterSound("Why", "Why2.mp3")
        RegisterSound("Power", "Power.mp3")
        RegisterSprite("ShockedSeb", "Planes/SebAsset2.png")
        RegisterSprite("boss", "Planes/BigBoss.png")
        RegisterSprite("Explosion/0", "Explosion/frame1.png")
        RegisterSprite("Explosion/1", "Explosion/frame2.png")
        RegisterSprite("Explosion/2", "Explosion/frame3.png")
        RegisterSprite("Explosion/3", "Explosion/frame4.png")
        RegisterSprite("Explosion/4", "Explosion/frame5.png")
        RegisterSprite("Explosion/5", "Explosion/frame6.png")
        RegisterSprite("bullet", "Bullet.png")
        RegisterSprite("defaultEnemy", "smallGreenPlane.png")
        RegisterSprite("collideEnemy", "FatGreyPlane.png")
        RegisterSprite("Powerup", "Pow.png")
        RegisterSprite("Powerup2", "Pow2.png")
        RegisterSprite("Pow2Vis", "PowerUpVis.png")
        LoadChars()
        pg.mixer.music.load("./Assets/music_main.mp3")
        pg.mixer.music.play(-1)
        

        #Window.WINDOW._game._powerUps.append(Pow(0, 0))

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
        
        if Input.GetKeyDown(pg.K_v):
            if self._player._godmode == True:
                Pow2.usePowerup()
            elif self._pow2Num > 0:
                Pow2.usePowerup()
                self._pow2Num -= 1
                print(str(self._pow2Num))
        if Input.GetKeyDown(pg.K_x):
            if self._player._godmode == True:
                PlaySound("Why")
                if self._pow2Num < 3:
                    self._pow2Num += 1

        if Input.GetKeyDown(pg.K_c):
            if self._player._godmode == True:
                self._pow = True

        if Input.GetKeyDown(pg.K_PERIOD):
            if self._player._godmode ==True:
                if self._wave == 1:
                    self._wave += 8
                else:
                    self._wave += 9
        
        if Input.GetKeyDown(pg.K_SLASH):
            if self._player._godmode ==True:
                self._wave += 5
        
        if Input.GetKeyDown(pg.K_COMMA):
            if self._player._godmode == True:
                if self._wave >= 5:
                    self._wave -= 5
        if Input.GetKeyDown(pg.K_ESCAPE):
            self._menu.Reset()
            self._SkipMenu = False
        
        if Input.GetKeyDown(pg.K_z):
            self._showDebug = not self._showDebug

        

        if Input.GetKeyDown(pg.K_i):
            self._player._godmode = not self._player._godmode
        if self._player._godmode:
            self._EnteredGodMode = True

        mousePos = pg.mouse.get_pos()

        '''
        if Input.GetKeyDown(pg.K_v):
            MakeBulletCircle(mousePos[0] / 2, mousePos[1] / 2, 25)
        '''

        self._background.draw(deltaTime, time)
        
        if Input.GetKeyDown(pg.K_2):
            print(mousePos)


        if self._waveTime <= 0:

            spawnedBoss = False

            if self._boss == None:
                if(self._wave + 1) % 10 + self._bossSpawnIncrease == 0:
                    self._bossesSpawned += 1
                    self._boss = Boss(30, -LoadSprite("boss").get_height()-10, round(self._nextBossHealth + 30), 10 + self._bossesSpawned - 1)
                    spawnedBoss = True
                    self._wave += 1
                    self._nextBossHealth = round((self._nextBossHealth + 40) * 1.1)
                    self._waveTime = self._startWaveTime
                    for i in range(self._wave):
                        if self._decreaseWaveTime:
                            if self._timeBetweenWaves > self._stopScalingAt:
                                self._waveTime *= 1 - (self._waveTime) / self._scaling
                            else:
                                self._waveTime = self._stopScalingAt
                        else:
                            self._waveTime = self._timeBetweenWaves
                    self._timeBetweenWaves = self._waveTime
                    self._wavesSinceLastCount += 1

                    if (self._wave + 1) % 20 == 0:
                        self._bossSpawnIncrease += 10 * (self._bossesSpawned / 2)

                    if self._wavesSinceLastCount >= self._wavesBetweenCountUp:
                        self._maxEnemiesPerWave += 1
                        self._minEnemiesPerWave += 1
                        self._wavesBetweenCountUp *= 1.5
                        self._wavesSinceLastCount = 0

                    if self._colEnemyChance < self._maxColChance:
                        self._colEnemyChance = self._wave / 10
                    else:
                        self._colEnemyChance = self._maxColChance

                if spawnedBoss == False:
                    for i in range(round(rand()) * (self._maxEnemiesPerWave - self._minEnemiesPerWave) + self._minEnemiesPerWave):
                        if round(rand() * 10) <= self._colEnemyChance and self._wave > 3:
                            self._collisionEnemies.append(CollisionEnemy(rand() * 200, rand() * -100))
                        else:
                            self._enemies.append(Enemy(rand() * 200, rand() * -100))
                    self._wave += 1
                    self._waveTime = self._startWaveTime
                    for i in range(self._wave):
                        if self._decreaseWaveTime:
                            if self._timeBetweenWaves > self._stopScalingAt:
                                self._waveTime *= 1 - (self._waveTime) / self._scaling
                            else:
                                self._waveTime = self._stopScalingAt
                        else:
                            self._waveTime = self._timeBetweenWaves
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

        if self._pow:
            self._powTime += deltaTime
            if self._powTime > 10:
                self._pow = False
                self._powTime = 0

        if self._spawnWaves:
            self._waveTime -= deltaTime
        #Player Bullet Stuff
        if Input.GetKeyDown(pg.K_SPACE):
            if self._player.doRender == True:
                if self._cooldown <= 0:
                    if self._shotcount >= 3:
                        self._cooldown = 0.2
                        self._shotcount = 0
                    self._shotcount += 1
                    if self._pow == True:
                        self._bullets.append(Bullet(self._player.posX - 10, self._player.posY))
                        self._bullets.append(Bullet(self._player.posX - 3, self._player.posY))
                        self._bullets.append(Bullet(self._player.posX + 3, self._player.posY))
                        self._bullets.append(Bullet(self._player.posX + 10, self._player.posY))
                    else:
                        self._bullets.append(Bullet(self._player.posX - 5, self._player.posY))
                        self._bullets.append(Bullet(self._player.posX + 5, self._player.posY))
        if self._boss != None:
            self._boss.draw(deltaTime, time)

        self._cooldown -= deltaTime

        for explosion in self._explosions:
            explosion: Explosion
            if explosion.frame > 4:
                self._explosions.remove(explosion)
            else:
                explosion.draw(deltaTime, time)

        for bullet in self._bullets:
            bullet: Bullet
            #Where the enemies get killed
            for enemy in self._enemies:
                enemy: Enemy
                colSize = 18
                if abs(enemy.posX + colSize / 1.25 - bullet.posX) < colSize and abs(bullet.posX - enemy.posX) < colSize:
                    if abs(enemy.posY + colSize / 1.25 - bullet.posY) < colSize and abs(bullet.posY - enemy.posY) < colSize:
                        self._explosions.append(Explosion(enemy.posX, enemy.posY))
                        self._enemies.remove(enemy)
                        if bullet in self._bullets:
                            self._bullets.remove(bullet)
                        self._score += 10

                        if rand() * 100 <= 5: 
                            Window.WINDOW._game._powerUps.append(Pow(enemy.posX, enemy.posY))
                        #Do here
                        break
            for enemy in self._collisionEnemies:
                enemy : CollisionEnemy
                colSize = 25
                if abs(enemy.posX + colSize / 1.25 - bullet.posX) < colSize and abs(bullet.posX - enemy.posX) < colSize:
                    if abs(enemy.posY + colSize / 1.25 - bullet.posY) < colSize and abs(bullet.posY - enemy.posY) < colSize:
                        self._explosions.append(Explosion(enemy.posX, enemy.posY))
                        self._collisionEnemies.remove(enemy)
                        if bullet in self._bullets:
                            self._bullets.remove(bullet)
                        self._score += 10
                        if rand() * 100 <= 25:
                            Window.WINDOW._game._powerUps2.append(Pow2(enemy.posX, enemy.posY))
                        break
            
            if self._boss  != None:
                colSize = 75
                distanceToPlayerX = 100
                distanceToPlayerY = 100
                distanceToBoss = 100

                distanceToPlayerX = abs(self._boss.posX + 80 - bullet.posX)
                distanceToPlayerY = abs(self._boss.posY + 10 - bullet.posY)
                distanceToBoss = sqrt(distanceToPlayerX * distanceToPlayerX + distanceToPlayerY * distanceToPlayerY)
                if distanceToBoss < 70:
                    self._explosions.append(Explosion(bullet.posX, bullet.posY))
                    self._boss.health -= 1
                    if self._boss.bossSprite == 1:
                        PlaySound("Why")
                    if bullet in self._bullets:
                        self._bullets.remove(bullet)
                    self._score += 2
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

        for pow in self._powerUps:
            pow: Pow
            pow.draw(deltaTime, time)

        for pow2 in self._powerUps2:
            pow2: Pow2
            pow2.draw(deltaTime, time)

              
            

        for enemy in self._enemies:
            enemy: Enemy
            enemy.draw(deltaTime, time)
            
        for collisionEnemy in self._collisionEnemies:
            collisionEnemy : CollisionEnemy 
            collisionEnemy.draw(deltaTime, time)

        self._player.draw( deltaTime, time)


        if not self._EnteredGodMode:
        
            if self._score > self._highScore:
                self._highScore = self._score
        else:
            self._score = 0
        
        self._debugY = 0
        
        Pow2.renderPower()

        if self._showDebug:
            

            self.DrawDebugText("SCORE: " + str(self._score), (255, 255, 255))
            
            self.DrawDebugText("HIGH SCORE: " + str(self._highScore), (255, 255, 255))

            
            self.DrawDebugText("WAVE TIME: " + str(round(self._waveTime, 2)), (255, 255, 255))

            DrawText("X: " + str(floor(self._player.posX)), 0, self._debugY, (0, 0, 255))
            DrawText("Y: " + str(floor(self._player.posY)), 0 + GetTextWidth("X: 999"), self._debugY, (0, 0, 255))
            self._debugY += GetTextHeight("X: " + str(floor(self._player.posX)) + "Y: " + str(floor(self._player.posY)))
            

            self.DrawDebugText("ENEMY COUNT: " + str(len(self._enemies)), (255, 255, 255))
            
            
            self.DrawDebugText("ENEMY BULLET NUM: " + str(len(self._enemyBullets)), (255, 255, 255))
            self.DrawDebugText("PLAYER BULLET NUM: " + str(len(self._bullets)), (255, 255, 255))


            if self._player._godmode:
                self.DrawDebugText("GOD MODE: TRUE", (0, 255, 0))

            else:
                self.DrawDebugText("GOD MODE: FALSE", (255, 0, 0))

            self.DrawDebugText("WAVE: " + str(self._wave), (255, 255, 255))


            totalWaveTime = self._timeBetweenWaves
            self.DrawDebugText("TOTAL WAVE TIME: " + str(round(totalWaveTime, 2)), (255, 255, 255))
            self.DrawDebugText("FPS: " + str(round(Window.WINDOW.clock.get_fps(), 1)), (255, 0, 0))
            self.DrawDebugText("POW COUNT: " + str(len(self._powerUps)), (255, 255, 255))
            self.DrawDebugText("POW TIME: " + str(round(self._powTime, 2)), (255, 255, 255))

            if self._boss != None:
                self.DrawDebugText(" ", (255, 255, 255))
                self.DrawDebugText("BOSS", (255, 255, 255))
                self.DrawDebugText("HEALTH: " + str(self._boss.health), (255, 255, 255))

        
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
    
