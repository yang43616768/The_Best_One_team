import pygame
from random import randint
from setting import *

class Map:
    def __init__(self):
        self.images = [pygame.image.load(tile) for tile in Gamepath.groundTiles]
        self.images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.images]
        self.map = self.gen_map()

    def gen_map(self):
        maporigin = []
        for i in range(SceneSettings.tileXnum):
            tmp = []
            for j in range(SceneSettings.tileYnum):
                tmp.append(self.images[randint(0, len(self.images) - 1)])
            maporigin.append(tmp)
        return maporigin