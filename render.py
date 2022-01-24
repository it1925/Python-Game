import numpy as np
import pygame as pg
from game import Game


# from walls import Walls

class Floorrender:
    SKYTEXTURE = pg.image.load('sky.jpg')
    SKY = pg.surfarray.array3d(pg.transform.scale(SKYTEXTURE, (360, Game.HalfVRes * 2)))
    FLOORTEXTURE = pg.surfarray.array3d(pg.image.load('floor.jpg'))
    WALLTEXTURE = pg.surfarray.array3d(pg.image.load('floor2.jpg'))
    posx, posy, rot = 0, 0, 0
    size = 15
    map = np.random.choice([0, 0, 0, 0, 1], (size, size))

    def __init__(self):

        for i in range(Game.Hres):
            rot_i = self.rot + np.deg2rad(i / Game.DIR - (Game.FOV / 2))
            sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i / Game.DIR - (Game.FOV / 2)))
            Game.FRAME[i][:] = self.SKY[int(np.rad2deg(rot_i) % 359)][:] / 255

            for j in range(Game.HalfVRes):
                n = (Game.HalfVRes / (Game.HalfVRes - j)) / cos2
                x = self.posy + sin * n
                y = self.posx + cos * n
                xx = int(x * 2 % 1 * 99)
                yy = int(y * 2 % 1 * 99)
                shade = 0.2 + 0.9 * (1 - j / Game.HalfVRes)
                if shade > 0.7:
                    shade = 0.7

                if self.map[int(x)%(self.size-1)][int(y) % (self.size-1)]:
                    h = Game.HalfVRes - j
                    c = shade*np.ones(3)
                    for k in range(h*2):
                        if 0 <= Game.HalfVRes - h + k < 2 * Game.HalfVRes:
                            Game.FRAME[i][Game.HalfVRes - h + k] = c
                    break

                else:
                    Game.FRAME[i][Game.HalfVRes * 2 - j - 1] = shade * self.FLOORTEXTURE[xx][yy] / 255
