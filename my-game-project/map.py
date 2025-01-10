from random import randint
import pygame
from setting import *

class Map1:
    def __init__(self):
        self.images = [pygame.image.load(tile) for tile in Gamepath.groundTiles1]
        self.images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.images]
        self.map = self.gen_map()

    def gen_map(self):
        maporigin = []
        for i in range(SceneSettings.tileXnum):
            tmp = []
            for j in range(SceneSettings.tileYnum):
                tmp.append(randint(0, len(self.images) - 1))  # 使用索引而不是图像
            maporigin.append(tmp)
        return maporigin

class Map2:
    def __init__(self):
        self.images = [pygame.image.load(tile) for tile in Gamepath.groundTiles2]
        self.images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.images]
        self.map = self.gen_map()

    def gen_map(self):
        maporigin = []
        for i in range(SceneSettings.tileXnum):
            tmp = []
            for j in range(SceneSettings.tileYnum):
                tmp.append(randint(0, len(self.images) - 1))  # 使用索引而不是图像
            maporigin.append(tmp)
        return maporigin
    
