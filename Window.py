
import pygame as pg

from Input import *
from Body import *

from Game import *

class Window:

    _display = None

    _width = 0
    _height = 1
    _title = ""

    _input = None

    def __init__(self, title, width, height):
        self._title = title
        self._width = width
        self._height = height
        self._input = Input(self)
        pass

    def Create(self):
        pg.init()
        self._display = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption(self._title)

        clock = pg.time.Clock()

        closed = False

        time = 0;


        Start()

        while not closed:

            for event in pg.event.get():
                self._input.PollEvents(event);
                if event.type == pg.QUIT:
                    closed = True

            self._display.fill((0, 0, 0))
            
            Update()

            self._input._newdownKeys.clear()
        
            pg.display.update()

            time = time + clock.get_time()

            clock.tick(60)

        pg.quit()
        quit()