
import pygame as pg


import Window



soundRegistry = {}

def RegisterSound(id, file):
    soundRegistry.update({id: pg.mixer.Sound("./assets/" + file)})
    pg.mixer.Sound.set_volume(LoadSound(id), 0.25)

def LoadSound(id) -> pg.mixer.Sound:
    if id not in soundRegistry:
        print("ERROR: Registry does not contain sound (\"" + id + "\")")
        return None
    return soundRegistry[id]

def PlaySound(id: str):
    if not Window.WINDOW._game._Muted:
        
        pg.mixer.Sound.play(LoadSound(id))