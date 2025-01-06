from random import randint
import pygame
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
                tmp.append(randint(0, len(self.images) - 1))  # 使用索引而不是图像
            maporigin.append(tmp)
        return maporigin

# def gen_map():
#     images = [pygame.image.load(tile) for tile in Gamepath.groundTiles]
#     images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

#     maporigin = []
#     for  i in range(SceneSettings.tileXnum):
#         tmp = []
#         for j in range(SceneSettings.tileYnum):
#             tmp.append(images[randint(0,len(images)-1)])
#         maporigin.append(tmp)

#     return maporigin