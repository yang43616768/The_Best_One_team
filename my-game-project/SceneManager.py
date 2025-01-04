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
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width / WindowsSettings.OutdoorScale, WindowsSettings.height / WindowsSettings.OutdoorScale)

    def tick(self, fps):
        self.clock.tick(fps)
    
    def get_width(self):
        return WindowsSettings.width * WindowsSettings.OutdoorScale
    
    def get_height(self):
        return WindowsSettings.height * WindowsSettings.OutdoorScale
    
    def location(self, obj):
        if isinstance(obj, pygame.sprite.Group):
            for sprite in obj:
                self.window.blit(sprite.image, (sprite.rect.x - WindowsSettings.OutdoorScale * self.camera.x, sprite.rect.y - WindowsSettings.OutdoorScale * self.camera.y))
        elif isinstance(obj, Player) :
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        elif isinstance(obj, NPC):
            self.window.blit(obj.image, (obj.rect.x - WindowsSettings.OutdoorScale * self.camera.x, obj.rect.y - WindowsSettings.OutdoorScale * self.camera.y))
        else:
            pass
        if isinstance(obj, NPC) and obj.dialogue_active:
            obj.draw_dialogue(self.window)
        if isinstance(obj,NPC) and obj.buy_active:
            obj.draw_buy(self.window)
        if isinstance(obj,NPC) and obj.fight_active:
            obj.draw_fight(self.window)
        if isinstance(obj,NPC) and obj.quest_active:
            obj.draw_bubble(self.window)


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
        buffer_x = self.camera.width / 3
        buffer_y = self.camera.height / 3

        if player.rect.x < self.camera.x + buffer_x:
            self.cameraX = player.rect.x - buffer_x
        elif player.rect.x > self.camera.x + WindowsSettings.width - buffer_x - PlayerSettings.playerWidth:
            self.cameraX = player.rect.x - WindowsSettings.width + buffer_x + PlayerSettings.playerWidth

        if player.rect.y < self.camera.y + buffer_y:
            self.cameraY = player.rect.y - buffer_y
        elif player.rect.y > self.camera.y + WindowsSettings.height - buffer_y - PlayerSettings.playerHeight:
            self.cameraY = player.rect.y - WindowsSettings.height + buffer_y + PlayerSettings.playerHeight

        # 确保摄像机不会超出地图边界
        max_camera_x = SceneSettings.tileXnum * SceneSettings.tileWidth - self.camera.width
        max_camera_y = SceneSettings.tileYnum * SceneSettings.tileHeight - self.camera.height

        self.cameraX = max(0, min(self.cameraX, max_camera_x))
        self.cameraY = max(0, min(self.cameraY, max_camera_y))

        self.camera.topleft = (self.cameraX, self.cameraY)