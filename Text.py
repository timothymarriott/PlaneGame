from SpriteRegistry import *

CHARACTERSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:. "


def LoadChars():

    for c in CHARACTERSET:
        if c == ':'[0]:
            #I didnt pick that updown dot name
            RegisterSprite("Character/:", "Characters/up_down_dot.png")
        elif c == '.'[0]:
            #I didnt pick that updown dot name
            RegisterSprite("Character/.", "Characters/dot.png")
        elif c == ' '[0]:
            continue
        else:
            RegisterSprite("Character/" + c, "Characters/" + c + ".png")

def DrawText(text, x: int, y: int, color):
    currX: int = 0
    for c in text:
        if not c in CHARACTERSET:
            continue
        if c == ' '[0]:
            currX += LoadSprite("Character/A").get_width()
        elif c == '.'[0]:
            DrawTintedSprite("Character/" + c, x + currX, y+LoadSprite("Character/A").get_height() - LoadSprite("Character/" + c).get_height(), color)
            currX += LoadSprite("Character/" + c).get_width()
        else:
            DrawTintedSprite("Character/" + c, x + currX, y, color)
            currX += LoadSprite("Character/" + c).get_width()

def GetTextWidth(text) -> int:
    currX: int = 0
    for c in text:
        if not c in CHARACTERSET:
            continue
        if c == ' '[0]:
            currX += LoadSprite("Character/A").get_width()
        else:
            currX += LoadSprite("Character/" + c).get_width()
    return currX

def GetTextHeight(text) -> int:
    
    if text[0] == " ":
        height = LoadSprite("Character/A").get_height()
    else:
        height = LoadSprite("Character/" + text[0]).get_height()
    return height




