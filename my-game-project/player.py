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
            if self.rect.x > WindowsSettings.width * 1.5 - PlayerSettings.playerWidth:
                self.rect.x = WindowsSettings.width * 1.5 - PlayerSettings.playerWidth
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > WindowsSettings.height * 1.5 - PlayerSettings.playerHeight:
                self.rect.y = WindowsSettings.height * 1.5 - PlayerSettings.playerHeight



    def draw(self,window):
        window.blit(self.image, self.rect)

    def add_item(self, item):
        self.inventory.append(item)
        Item_List.items[item].statistics_adding(self)