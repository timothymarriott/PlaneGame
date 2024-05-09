
import pygame as pg

spriteRegistry = {}

def RegisterSprite(id, file):
    spriteRegistry.update({id: pg.image.load("./assets/" + file)})

def LoadSprite(id) -> pg.Surface:
    if id not in spriteRegistry:
        print("ERROR: Registry does not contain sprite")
        return
    return spriteRegistry[id]

def DrawSprite(screen: pg.surface.Surface, id: str, x: int, y: int):
    screen.blit(LoadSprite(id), (x, y))
    