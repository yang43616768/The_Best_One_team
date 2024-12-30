from setting import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(......)
        self.image = pygame.transform.scale(self.image, (PlayerSettings.width, PlayerSettings.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PlayerSettings.playerSpeed
        self.health = PlayerSettings.playerHealth
        self.defense = PlayerSettings.PlayerDefense
        self.attack = PlayerSettings.playerAttack
        self.moves = PlayerSettings.PlayerMoves

    def update(self,walls):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if keys[pygame.K_LEFT]:
                    self.rect.x += self.speed
                if keys[pygame.K_RIGHT]:
                    self.rect.x -= self.speed
                if keys[pygame.K_UP]:
                    self.rect.y += self.speed
                if keys[pygame.K_DOWN]:
                    self.rect.y -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WindowsSettings.width - PlayerSettings.width:
            self.rect.x = WindowsSettings.width - PlayerSettings.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > WindowsSettings.height - PlayerSettings.height:
            self.rect.y = WindowsSettings.height - PlayerSettings.height