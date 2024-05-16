from Input import Input
import pygame as pg
from SpriteRegistry import *

class Background:

    posY = 0

    _speed = 25

    def __init__(self) -> None:
        RegisterSprite("terrain_main", "terrain_main.png")
        pass

    def draw(self, deltaTime: float, time: float):
        self.posY += self._speed * deltaTime
        DrawSprite("terrain_main", 0, self.posY % LoadSprite("terrain_main").get_height())
        DrawSprite("terrain_main", 0, self.posY % LoadSprite("terrain_main").get_height() - LoadSprite("terrain_main").get_height())
        pass