from SpriteRegistry import *

CHARACTERSET = "ABCDEFGHIJKLMOPQRSTUVWXYZ0123456789"


def LoadChars():

    for c in CHARACTERSET:
        RegisterSprite("Character/" + c, "Characters/" + c + ".png")

def DrawText(text, x: int, y: int, color):
    currX: int = 0
    for c in text:
        if c == ' '[0]:
            currX += LoadSprite("Character/A").get_width()
        else:
            DrawTintedSprite("Character/" + c, x + currX, y, color)
            currX += LoadSprite("Character/" + c).get_width()

def GetTextWidth(text) -> int:
    currX: int = 0
    for c in text:
        if c == ' '[0]:
            currX += LoadSprite("Character/A").get_width()
        else:
            currX += LoadSprite("Character/" + c).get_width()
    return currX

def GetTextHeight(text) -> int:
    
    height = LoadSprite("Character/" + text[0]).get_height()
    return height




