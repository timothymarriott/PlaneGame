from SpriteRegistry import *

CHARACTERSET = "ABCDEFGHIJKLMOPQRSTUVWXYZ0123456789"


def LoadChars():

    for c in CHARACTERSET:
        RegisterSprite("Character/" + c, "Characters/" + c + ".png")

def DrawText(text, x: int, y: int):
    currX: int = 0
    for c in text:
        DrawSprite("Character/" + c, x + currX, y)
        currX += LoadSprite("Character/" + c).get_width()

def GetTextWidth(text) -> int:
    currX: int = 0
    for c in text:
        currX += LoadSprite("Character/" + c).get_width()
    return currX





