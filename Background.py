from Input import Input
import pygame as pg
from SpriteRegistry import *

class Background:

    posY = 0

    _speed = 25

    def __init__(self) -> None:
        RegisterSprite("terrain_main", "terrain_main.png")
        pass

    def draw(self, screen: pg.surface.Surface, deltaTime: float, time: float):
        self.posY += self._speed * deltaTime
        DrawSprite(screen, "terrain_main", 0, self.posY % LoadSprite("terrain_main").get_height())
        DrawSprite(screen, "terrain_main", 0, self.posY % LoadSprite("terrain_main").get_height() - LoadSprite("terrain_main").get_height())
        pass