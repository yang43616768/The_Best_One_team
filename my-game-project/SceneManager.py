from setting import *
import pygame
import map
from player import *
from npc import *
from wall import *


# class SceneManager:
#     def __init__(self, window):
#         self.map = map.gen_map()
#         self.window = window
#         self.clock = pygame.time.Clock()
#         self.cameraX = 0
#         self.cameraY = 0
#         # 调整摄像机的宽度和高度为地图的1/4
#         self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width / 2, WindowsSettings.height / 2)

#     def tick(self, fps):
#         self.clock.tick(fps)
    
#     def get_width(self):
#         return WindowsSettings.width * WindowsSettings.OutdoorScale
    
#     def get_height(self):
#         return WindowsSettings.height * WindowsSettings.OutdoorScale
    
#     def location(self, obj):
#         if isinstance(obj, pygame.sprite.Group):
#             obj.draw(self.window)
#         elif isinstance(obj, Player) or isinstance(obj, NPC):
#             obj.draw(self.window)
#         if isinstance(obj,NPC) and obj.dialogue_active:
#             obj.draw_dialogue(self.window)

#     def render(self):
#         for i in range(SceneSettings.tileXnum):
#             for j in range(SceneSettings.tileYnum):
#                 self.window.blit(self.map[i][j], (SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))

#     def update_camera(self, player):
#         self.cameraX = player.rect.x - WindowsSettings.width / 4
#         self.cameraY = player.rect.y - WindowsSettings.height / 4
#         # 更新摄像机的宽度和高度为地图的1/4
#         self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width / 2, WindowsSettings.height / 2)
#         self.window.blit(self.background, (0, 0), self.camera)

class SceneManager:
    def __init__(self, window):
        self.map = map.gen_map()
        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        # 调整摄像机的宽度和高度为地图的1/4
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width / 2, WindowsSettings.height / 2)

    def tick(self, fps):
        self.clock.tick(fps)

    def get_width(self):
        return WindowsSettings.width * WindowsSettings.OutdoorScale

    def get_height(self):
        return WindowsSettings.height * WindowsSettings.OutdoorScale

    def location(self, obj):
        if isinstance(obj, pygame.sprite.Group):
            obj.draw(self.window)
        elif isinstance(obj, Player) or isinstance(obj, NPC):
            obj.draw(self.window)
        if isinstance(obj, NPC) and obj.dialogue_active:
            obj.draw_dialogue(self.window)

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                tile = self.map[i][j]
                tile_rect = tile.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                if self.camera.colliderect(tile_rect):
                    self.window.blit(tile, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))

    def update_camera(self, player):
        self.cameraX = player.rect.x - self.camera.width / 2
        self.cameraY = player.rect.y - self.camera.height / 2
        # 更新摄像机的宽度和高度为地图的1/4
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width / 2, WindowsSettings.height / 2)