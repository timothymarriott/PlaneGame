
import pygame as pg

from Window import WINDOW

spriteRegistry = {}

def RegisterSprite(id, file):
    spriteRegistry.update({id: pg.image.load("./assets/" + file)})

def LoadSprite(id) -> pg.Surface:
    if id not in spriteRegistry:
        print("ERROR: Registry does not contain sprite")
        return
    return spriteRegistry[id]

def DrawSprite(id: str, x: int, y: int):
    
    WINDOW._screen.blit(LoadSprite(id), (x, y))
    