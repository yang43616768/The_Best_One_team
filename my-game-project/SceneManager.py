from setting import *
import pygame
from map import *
from setting import Gamepath, SceneSettings # 从setting.py中导入Gamepath和SceneSettings
from player import *
from npc import *   
from wall import *
from portal import *
from transparent import *

class SceneManager:
    def __init__(self, window):
        self.map1 = Map1()
        self.map2 = Map2()
        self.tiles1 = self.map1.gen_map()
        self.tile_images1 = [pygame.image.load(tile) for tile in Gamepath.groundTiles1]
        self.tile_images1 = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.tile_images1]
        self.tiles = self.map2.gen_map()
        self.tile_images2 = [pygame.image.load(tile) for tile in Gamepath.groundTiles2]
        self.tile_images2 = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in self.tile_images2]

        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        # 调整摄像机的宽度和高度为地图的1/4
        self.camera = pygame.Rect(self.cameraX, self.cameraY, WindowsSettings.width , WindowsSettings.height)
        # self.transparent_objects = [] # 存储透明对象

    def tick(self, fps):
        self.clock.tick(fps)
    
    def get_width(self):
        return WindowsSettings.width
    
    def get_height(self):
        return WindowsSettings.height
    
    # def add_transparent_object(self, transparent_object):
    #     self.transparent_objects.append(transparent_object)
    
    # def render_transparent(self):
    #     for obj in self.transparent_objects:
    #         obj.surface.blit(obj.image, (0, 0))
    #         obj.surface.set_alpha(obj.alpha)
    #         self.screen.blit(obj.surface, (obj.x, obj.y))

    def location(self, obj, npcs):
        npcs_not_active = not any(npc.dialogue_active for npc in npcs) and not any(npc.buy_active for npc in npcs) and not any(npc.fight_active for npc in npcs)
        # 根据对象类型将其绘制到窗口上
        if isinstance(obj, pygame.sprite.Group):
            # 如果对象是精灵组，则遍历每个精灵并绘制
            for sprite in obj:
                self.window.blit(sprite.image, (sprite.rect.x - self.camera.x, sprite.rect.y - self.camera.y))
        elif isinstance(obj, Player):
            # 如果对象是玩家，则绘制玩家图像
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        elif isinstance(obj, NPC) and npcs_not_active:
            # 如果对象是NPC，并且没有任何NPC处于对话、购买或战斗状态，则绘制NPC图像
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        elif isinstance(obj,Portal) and npcs_not_active:
            # 如果对象是Portal，则绘制Portal图像
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
        elif isinstance(obj, Transparent) and npcs_not_active:
            # 如果对象是 Transparent 类的实例，则渲染透明对象
            temp_surface = obj.image.copy()
            temp_surface.set_alpha(obj.alpha)
            self.window.blit(temp_surface, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))
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
        if isinstance(obj, Bubble) and obj.npc.quest_active and npcs_not_active:
            self.window.blit(obj.image, (obj.rect.x - self.camera.x, obj.rect.y - self.camera.y))

    def render1(self,npcs):
        # 创建一个临时表面，用于渲染摄像机视角内的内容
        temp_surface = pygame.Surface((self.camera.width, self.camera.height)) 
        if not any (npc.dialogue_active for npc in npcs) and not any (npc.buy_active for npc in npcs) and not any (npc.fight_active for npc in npcs):
            # 渲染地图
            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    tile_type = self.tiles[i][j]
                    tile_image = self.tile_images1[tile_type]
                    tile_rect = tile_image.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                    if self.camera.colliderect(tile_rect):
                        temp_surface.blit(tile_image, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))

        # 将临时表面渲染到窗口上
            self.window.blit(temp_surface, (0, 0))

        else:
            # 渲染地图
            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    tile_type = self.tiles[i][j]
                    tile_image = self.tile_images1[tile_type]
                    tile_rect = tile_image.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                    if self.camera.colliderect(tile_rect):
                        temp_surface.blit(tile_image, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))
            self.window.blit(temp_surface, (0, 0))

    def render2(self,npcs):
        # 创建一个临时表面，用于渲染摄像机视角内的内容
        temp_surface = pygame.Surface((self.camera.width, self.camera.height)) 
        if not any (npc.dialogue_active for npc in npcs) and not any (npc.buy_active for npc in npcs) and not any (npc.fight_active for npc in npcs):
            # 渲染地图
            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    tile_type = self.tiles[i][j]
                    tile_image = self.tile_images2[tile_type]
                    tile_rect = tile_image.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                    if self.camera.colliderect(tile_rect):
                        temp_surface.blit(tile_image, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))

        # 将临时表面渲染到窗口上
            self.window.blit(temp_surface, (0, 0))

        else:
            # 渲染地图
            for i in range(SceneSettings.tileXnum):
                for j in range(SceneSettings.tileYnum):
                    tile_type = self.tiles[i][j]
                    tile_image = self.tile_images2[tile_type]
                    tile_rect = tile_image.get_rect(topleft=(SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                    if self.camera.colliderect(tile_rect):
                        temp_surface.blit(tile_image, (tile_rect.x - self.camera.x, tile_rect.y - self.camera.y))
            self.window.blit(temp_surface, (0, 0))

    def render3(self,npcs):
        temp_surface = pygame.Surface((self.camera.width, self.camera.height)) 

        background_image = pygame.image.load(r".\assets\images\stage2background.png")
        background_image = pygame.transform.scale(background_image, (2*WindowsSettings.width, 2*WindowsSettings.height))
        temp_surface.blit(background_image,(-self.camera.x, -self.camera.y))
        # 绘制背景图片，根据 camera 偏移值
        self.window.blit(temp_surface, (0, 0))
        



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