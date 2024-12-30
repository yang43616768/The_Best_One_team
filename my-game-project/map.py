import pygame
from random import random,randint
from setting import *

def build_obstacle():
    pass

def gen_map():
    images = [pygame.image.load(tile) for tile in Gamepath.groundTiles]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    maporigin = []
    for  i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0,len(images)-1)])
        maporigin.append(tmp)

    return maporigin