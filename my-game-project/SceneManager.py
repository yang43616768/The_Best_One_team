from setting import *
import pygame
from map import *
from setting import Gamepath, SceneSettings # 从setting.py中导入Gamepath和SceneSettings
from player import *
from npc import *   
from wall import *

class SceneManager:
    def __init__(self, window):
        self.map = Map()
        self.tiles = self.map.gen_map()
        self.tile_images = [pygame.image.load(tile) for tile in Gamepath.groundTiles]
        self.tile_images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.tile_images]
        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        # 调整摄像机的宽度和高度为地图的1/4
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width , WindowsSettings.height)

    def tick(self, fps):
        self.clock.tick(fps)
    
    def get_width(self):
        return WindowsSettings.width
    
    def get_height(self):
        return WindowsSettings.height
    
    def location(self, obj, npcs):
        # 根据对象类型将其绘制到窗口上
        if isinstance(obj, pygame.sprite.Group):
            # 如果对象是精灵组，则遍历每个精灵并绘制
            for sprite in obj:
                self.window.blit(sprite.image, (sprite.rect.x - self.camera.x, sprite.rect.y - self.camera.y))
        elif isinstance(obj, Player):
            # 如果对象是玩家，则绘制玩家图像
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        elif isinstance(obj, NPC) and not any(npc.dialogue_active for npc in npcs) and not any(npc.buy_active for npc in npcs) and not any(npc.fight_active for npc in npcs):
            # 如果对象是NPC，并且没有任何NPC处于对话、购买或战斗状态，则绘制NPC图像
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        else:
            pass
        
        # 如果NPC处于对话状态，则绘制对话框
        if isinstance(obj, NPC) and obj.dialogue_active:
            obj.draw_dialogue(self.window)
        # 如果NPC处于购买状态，则绘制购买界面
        if isinstance(obj, NPC) and obj.buy_active:
            obj.draw_buy(self.window)
        # 如果NPC处于战斗状态，则绘制战斗界面
        if isinstance(obj, NPC) and obj.fight_active:
            obj.draw_fight(self.window)
        # 如果NPC处于任务状态，并且不处于对话、购买或战斗状态，则绘制任务气泡
        if isinstance(obj, NPC) and obj.quest_active and not obj.dialogue_active and not obj.buy_active and not obj.fight_active:
            obj.draw_bubble(self.window)
        
    def render(self):
        # 创建一个临时表面，用于渲染摄像机视角内的内容
        temp_surface = pygame.Surface((self.camera.width, self.camera.height)) 
        # 渲染地图
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                tile_type = self.tiles[i][j]
                tile_image = self.tile_images[tile_type]
                tile_rect = tile_image.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                if self.camera.colliderect(tile_rect):
                    temp_surface.blit(tile_image, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))
            
        # # 渲染红色色块（固定在地图上）
        # red_blocks = [
        #     (1000, 800, 50, 50),
        #     (100, 800, 50, 50)
        # ]
        # for block in red_blocks:
        #     block_rect = pygame.Rect(block)
        #     if self.camera.colliderect(block_rect):
        #         pygame.draw.rect(temp_surface, (255, 0, 0), (block_rect.x - self.camera.x, block_rect.y - self.camera.y, block_rect.width, block_rect.height))
        
        # 将临时表面渲染到窗口上
        self.window.blit(temp_surface, (0, 0))
        pygame.display.flip()

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