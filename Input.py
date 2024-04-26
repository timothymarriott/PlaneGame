import pygame as pg


class Input:

    _window = None

    _downKeys = []

    def __init__(self, window) -> None:

        _window = window

        pass

    def PollEvents(self, events: pg.event.Event):
        if events.type == pg.KEYDOWN:
            self._downKeys.append(events.dict["key"])
        elif events.type == pg.KEYUP:
            self._downKeys.remove(events.dict["key"])
       
    @staticmethod
    def GetKey(key) -> bool:
        return key in Input._downKeys