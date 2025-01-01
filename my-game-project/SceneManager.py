from setting import *
import pygame
import map
from player import *
from npc import *
from wall import *

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
            for sprite in obj:
                self.window.blit(sprite.image, (sprite.rect.x - self.camera.x, sprite.rect.y - self.camera.y))
        elif isinstance(obj, Player) or isinstance(obj, NPC):
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        if isinstance(obj, NPC) and obj.dialogue_active:
            obj.draw_dialogue(self.window)

    def render(self):
        # 创建一个临时表面，用于渲染摄像机视角内的内容
        temp_surface = pygame.Surface((self.camera.width, self.camera.height))
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                tile = self.map[i][j]
                tile_rect = tile.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                if self.camera.colliderect(tile_rect):
                    temp_surface.blit(tile, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))
        
        # 将临时表面缩放到窗口大小，并渲染到窗口上
        scaled_surface = pygame.transform.scale(temp_surface, (WindowsSettings.width, WindowsSettings.height))
        self.window.blit(scaled_surface, (0, 0))

    def update_camera(self, player):
        # 计算摄像机的新位置
        self.cameraX = player.rect.x - self.camera.width / 2
        self.cameraY = player.rect.y - self.camera.height / 2

        # 确保摄像机不会超出地图边界
        self.cameraX = max(0, min(self.cameraX, SceneSettings.tileXnum * SceneSettings.tileWidth - self.camera.width))
        self.cameraY = max(0, min(self.cameraY, SceneSettings.tileYnum * SceneSettings.tileHeight - self.camera.height))

        self.camera.topleft = (self.cameraX, self.cameraY)