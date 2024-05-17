
import pygame as pg


import Window



soundRegistry = {}

def RegisterSound(id, file):
    soundRegistry.update({id: pg.mixer.Sound("./assets/" + file)})

def LoadSound(id) -> pg.mixer.Sound:
    if id not in soundRegistry:
        print("ERROR: Registry does not contain sound (\"" + id + "\")")
        return None
    return soundRegistry[id]

def PlaySound(id: str):
    
    pg.mixer.Sound.play(LoadSound(id))