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



    def show_inventory(self, window):
        if self.bag_active:
            font = pygame.font.Font(None, 36)
            inventory_surface = pygame.Surface((1000, 500), pygame.SRCALPHA)
            inventory_surface.fill((255, 255, 255, 180))  # 半透明白色背景
            y_offset = 10


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