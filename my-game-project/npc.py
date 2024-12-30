import pygame
from setting import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            self.image, (PlayerSettings.playerWidth, PlayerSettings.playerHeight)
        )
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def trigger_dialogue(self):
        