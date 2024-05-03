from Input import Input
import pygame as pg
from SpriteRegistry import *
from Background import Background
from Explosion import Explosion
from Player import Player



class Game:

    _background: Background = None
    _explosions = []

    _player: Player = None

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
        pass

    def Update(self, screen: pg.surface.Surface, deltaTime: float, time: float):
        if Input.GetKey(pg.K_a):
            print("tims got big massive")

        self._background.draw(screen, deltaTime, time)

        mousePos = pg.mouse.get_pos()

        if Input.GetKeyDown(pg.K_e):
            self._explosions.append(Explosion(mousePos[1] / 2, mousePos[0] / 2))

        for explosion in self._explosions:
            explosion: Explosion
            if explosion.frame > 4:
                self._explosions.remove(explosion)
                print("Killed Explosion")
            else:
                explosion.draw(screen, deltaTime, time)
                print("Drawing Explosion")

        self._player.draw(screen, deltaTime, time)
        
        return
    