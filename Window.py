
import pygame as pg

from Input import *
from Body import *

from Game import *

from SpriteRegistry import *

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

    closed = False

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
        pg.display.set_icon(pg.image.load("./assets/window-icon.png"))
        self._display = pg.display.set_mode((self._width, self._height))

        pg.display.set_caption(self._title)

        self.clock = pg.time.Clock()

        self.closed = False

        time = 0

        self._screen = pg.surface.Surface((self._actualWidth, self._actualHeight))

        self._game = Game()


        self._game.Start()

        while not self.closed:

            for event in pg.event.get():
                self._input.PollEvents(event);
                if event.type == pg.QUIT:
                    self.closed = True

            self._display.fill((0, 0, 0))
            
            self._screen.fill((0, 0, 0))

            self._game.Update(self.clock.get_time()/1000, time)

            screen = pg.transform.scale(self._screen, (self._width, self._height))

            self._display.blit(screen, (0, 0))

            self._input._newdownKeys.clear()
        
            pg.display.update()

            time = time + self.clock.get_time()

            self.clock.tick(60)

        self._game.End()

        pg.quit()

    

def GET() -> Window:
    return WINDOW

def DeltaTime() -> float:
    return WINDOW.clock.get_time()/1000