
import pygame as pg

from Input import *
from Body import *

from Game import *

class Window:

    _display = None

    _width = 0
    _actualWidth = 223
    _height = 1
    _actualHeight = 293
    _title = ""

    _input = None

    _screen = None

    _game: Game = None

    clock: pg.time.Clock = None

    def __init__(self, title, width, height):
        global WINDOW
        WINDOW = self
        self._title = title
        self._width = width
        self._height = height
        self._input = Input(self)
        
        pass

    

    def Create(self):
        pg.init()
        self._display = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption(self._title)

        self.clock = pg.time.Clock()

        closed = False

        time = 0

        self._screen = pg.surface.Surface((self._actualWidth, self._actualHeight))

        self._game = Game()


        self._game.Start()

        while not closed:

            for event in pg.event.get():
                self._input.PollEvents(event);
                if event.type == pg.QUIT:
                    closed = True

            self._display.fill((0, 0, 0))
            
            self._screen.fill((0, 0, 0))

            self._game.Update(self.clock.get_time()/1000, time)

            screen = pg.transform.scale(self._screen, (self._width, self._height))

            self._display.blit(screen, (0, 0))

            self._input._newdownKeys.clear()
        
            pg.display.update()

            time = time + self.clock.get_time()

            self.clock.tick(60)

        pg.quit()
        quit()

    

@staticmethod
def GET() -> Window:
    return WINDOW

@staticmethod
def DeltaTime() -> float:
    return WINDOW.clock.get_time()/1000