
import pygame as pg


import Window



spriteRegistry = {}

def RegisterSprite(id, file):
    spriteRegistry.update({id: pg.image.load("./assets/" + file)})

def LoadSprite(id) -> pg.Surface:
    if id not in spriteRegistry:
        print("ERROR: Registry does not contain sprite (\"" + id + "\")")
        return None
    return spriteRegistry[id]

def DrawSprite(id: str, x: int, y: int):
    
    Window.WINDOW._screen.blit(LoadSprite(id), (x, y))

def DrawTintedSprite(id: str, x: int, y: int, color):
    if LoadSprite(id) == None:
        return
    sprite = LoadSprite(id).copy()
    sprite.fill(color, special_flags=pg.BLEND_MULT)
    Window.WINDOW._screen.blit(sprite, (x, y))
    