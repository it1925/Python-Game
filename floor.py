import numpy as np
import pygame as pg
from game import Game


class Floorrender:
    SKYTEXTURE = pg.image.load('sky.jpg')
    SKY = pg.surfarray.array3d(pg.transform.scale(SKYTEXTURE, (360, Game.HalfVRes * 2)))
    FLOORTEXTURE = pg.surfarray.array3d(pg.image.load('floor.jpg'))
    posx, posy, rot = 0, 0, 0
    size = 3
    map = np.random.choice([0, 0, 0, 0, 1], (size, size))

    def __init__(self):
        for i in range(Game.Hres):
            rot_i = self.rot + np.deg2rad(i / Game.DIR - (Game.FOV / 2))
            sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i / Game.DIR - (Game.FOV / 2)))
            Game.FRAME[i][:] = self.SKY[int(np.rad2deg(rot_i) % 360)][:] / 255
            for j in range(Game.HalfVRes):
                n = (Game.HalfVRes / (Game.HalfVRes - j)) / cos2
                x = self.posy + sin * n
                y = self.posx + cos * n
                xx = int(x * 2 % 1 * 100)
                yy = int(y * 2 % 1 * 100)
                shade = 0.2 + 0.9 * (j / Game.HalfVRes)

                if self.map[int(x)%(self.size-1)][int(y) % (self.size-1)]:
                    h = Game.HalfVRes - j
                    c = shade*np.ones(3)
                    for k in range(h*2):
                        Game.FRAME[i][Game.HalfVRes - h + k] = c
                    break

                else:
                    Game.FRAME[i][Game.HalfVRes * 2 - j - 1] = shade * self.FLOORTEXTURE[xx][yy] / 255

                # if int(x)%2 == int(y)%2:
                #     Game.FRAME[i][Game.HalfVRes*2 - j - 1] = [0, 0, 0]
                # else:
                #     Game.FRAME[i][Game.HalfVRes*2 - j - 1] = [1, 1, 1]
