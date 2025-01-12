from setting import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(Gamepath.player)
        self.image = pygame.transform.scale(
            self.image, (PlayerSettings.playerWidth, PlayerSettings.playerHeight)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PlayerSettings.playerSpeed
        self.health = PlayerSettings.playerHealth
        self.defense = PlayerSettings.PlayerDefense
        self.attack = PlayerSettings.playerAttack
        self.moves = PlayerSettings.PlayerMoves
        self.currency = 100
        self.inventory = []
        self.bag_active = False
        self.scroll_offset = 0  # 初始化滚动偏移量
        self.item_message = None  # 用于存储获得物品的消息
        self.message_start_time = 0  # 用于记录消息显示的开始时间

    def update(self, walls,dialogue_active,buy_active, scene_manager):

        if not dialogue_active and not buy_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed

            # 检测与墙壁的碰撞
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if keys[pygame.K_a]:
                        self.rect.x += self.speed
                    if keys[pygame.K_d]:
                        self.rect.x -= self.speed
                    if keys[pygame.K_w]:
                        self.rect.y += self.speed
                    if keys[pygame.K_s]:
                        self.rect.y -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > WindowsSettings.width * 2 - PlayerSettings.playerWidth:
                self.rect.x = WindowsSettings.width * 2 - PlayerSettings.playerWidth
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > WindowsSettings.height * 2 - PlayerSettings.playerHeight:
                self.rect.y = WindowsSettings.height * 2 - PlayerSettings.playerHeight



    def draw(self,window):
        window.blit(self.image, self.rect)

    def add_item(self, item):
        self.inventory.append(item)
        if item in Item_List.keys:
            Item_List.items[item].statistics_adding(self)
        self.item_message = f"Obtained: {item}"
        self.message_start_time = pygame.time.get_ticks()


    def draw_item_message(self, window):
        if self.item_message is not None:
            current_time = pygame.time.get_ticks()
            if current_time - self.message_start_time < 2000:  # 显示两秒钟
                font = pygame.font.Font(None, 36)
                message_surface = pygame.Surface((700, 50), pygame.SRCALPHA)
                message_surface.fill((0, 0, 0, 180))  # 半透明黑色背景
                text_surface = font.render(self.item_message, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(350, 25))
                message_surface.blit(text_surface, text_rect)
                window.blit(message_surface, (window.get_width() // 2 - 350, window.get_height() // 2 + 225))
            else:
                self.item_message = None  # 超过两秒后清除消息

    def show_inventory(self, window):
        if self.bag_active:
            font = pygame.font.Font(None, 36)
            inventory_surface = pygame.Surface((1600, 900), pygame.SRCALPHA)
            inventory_surface.fill((173, 216, 230, 180))  # 半透明淡蓝色背景
            y_offset = 10 - self.scroll_offset  # 根据滚动偏移量调整 y_offset



            # 显示玩家属性
            attributes = [
                f"Health: {self.health}",
                f"Defense: {self.defense}",
                f"Attack: {self.attack}",
                f"Moves: {self.moves}",
                f"Currency: {self.currency}"
            ]
            for attribute in attributes:
                text_surface = font.render(attribute, True, (255, 255, 255))
                inventory_surface.blit(text_surface, (10, y_offset))
                y_offset += 30

            # 显示背包中的物品
            y_offset += 10
            for item in self.inventory:
                item_text = f'''{item} - {Item_List.items[item].discription} '''
                text_surface = font.render(item_text, True, (255, 255, 255))
                inventory_surface.blit(text_surface, (10, y_offset))
                y_offset += 30

            window.blit(inventory_surface, (50, 50))
        pygame.display.flip()