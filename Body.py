from Window import *

class Body:
    
    _window = None

    _posX = 0
    _posY = 0
    _size = (0, 0)
    _color = (255, 0, 255, 255)

    def __init__(self, window, pos, size = (100, 100), color = (255, 0, 255, 255)) -> None:
        self._pos = pos
        self._size = size
        self._color = color
        self._window = window
        pass

    def Draw(self):
        self._window._display.fill(self._color, (self._posX, self._posY, self._size[0], self._size[1]))

