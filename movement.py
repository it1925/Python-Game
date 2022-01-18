from floor import Floorrender
import pygame as pg
import numpy as np


class Movemetn:
    def __init__(self, keys, et):
        if keys[pg.K_LEFT] or keys[ord('a')]:
            Floorrender.rot = Floorrender.rot - 0.0003*et

        if keys[pg.K_RIGHT] or keys[ord('d')]:
            Floorrender.rot = Floorrender.rot + 0.0003*et

        if keys[pg.K_UP] or keys[ord('w')]:
            Floorrender.posx, Floorrender.posy = Floorrender.posx + np.cos(Floorrender.rot) * 0.0008*et, Floorrender.posy + np.sin(Floorrender.rot) * 0.0008*et

        if keys[pg.K_DOWN] or keys[ord('s')]:
            Floorrender.posx, Floorrender.posy = Floorrender.posx - np.cos(Floorrender.rot) * 0.0008*et, Floorrender.posy - np.sin(Floorrender.rot) * 0.0008*et
