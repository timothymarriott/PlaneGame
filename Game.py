from Input import Input
import pygame as pg
from SpriteRegistry import *
from Background import Background
from Explosion import Explosion
from Player import Player
from Bullet import Bullet
from Enemy import Enemy


class Game:

    _background: Background = None
    _explosions = []
    _bullets = []
    _enemies = []

    _player: Player = None

    _cooldown: float = 0
    _shotcount: int = 0


    def __init__(self) -> None:
        global GAME
        GAME = self
        pass
        

    def Start(self):
        self._background = Background()
        self._player = Player()
        RegisterSprite("Explosion/0", "Explosion/frame1.png")
        RegisterSprite("Explosion/1", "Explosion/frame2.png")
        RegisterSprite("Explosion/2", "Explosion/frame3.png")
        RegisterSprite("Explosion/3", "Explosion/frame4.png")
        RegisterSprite("Explosion/4", "Explosion/frame5.png")
        RegisterSprite("Explosion/5", "Explosion/frame6.png")
        RegisterSprite("bullet", "Bullet.png")
        pass

    def Update(self, screen: pg.surface.Surface, deltaTime: float, time: float):
        
        self._background.draw(screen, deltaTime, time)

        mousePos = pg.mouse.get_pos()

        if Input.GetKeyDown(pg.K_e):
            self._explosions.append(Explosion(mousePos[1] / 2, mousePos[0] / 2))

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
                explosion.draw(screen, deltaTime, time)
                print("Drawing Explosion")

        for bullet in self._bullets:
            bullet: Bullet
            bullet.draw(screen, deltaTime, time)
            
        for enemy in self._bullets:
            bullet: Bullet
            bullet.draw(screen, deltaTime, time)
            

        self._player.draw(screen, deltaTime, time)
        
        return
    
