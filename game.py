import numpy as np
import pygame as pg


class Game:
    FOV = 60
    SCREEN_W = 1200
    SCREEN_H = 800
    Hres = 120
    HalfVRes = 100
    DIR = Hres / FOV
    FRAME = np.random.uniform(0, 1, (Hres, HalfVRes * 2, 3))
    SURF = pg.surfarray.make_surface(FRAME * 255)
    CLOCK = pg.time.Clock()
    FPS = int(CLOCK.get_fps())

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running = True
        pg.display.set_caption('maze FPS: ' + str(self.FPS))

        self.loop()

    def update(self):
        self.surf = pg.surfarray.make_surface(self.FRAME * 255)
        self.surf = pg.transform.scale(self.surf, (self.SCREEN_W, self.SCREEN_H))

        self.screen.blit(self.surf, (0, 0))
        pg.display.update()

    def loop(self):
        while self.running:
            for event in pg.event.get():
                if event.type != pg.QUIT:
                    continue
                self.running = False
            Floorrender()

            self.update()
            Movemetn(pg.key.get_pressed(), self.CLOCK.tick())
        pg.quit()


from floor import Floorrender
from movement import Movemetn

Game()