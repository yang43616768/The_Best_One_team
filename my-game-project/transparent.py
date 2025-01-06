import pygame
class Transparent:
    def __init__(self,image_path,x,y,length,width):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (length, width))
        self.surface = pygame.Surface((length, width), pygame.SRCALPHA)
        self.alpha = 0
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def check_transparent(self,player):
        if self.rect.colliderect(player.rect):
            self.alpha = 100
        else:
            self.alpha = 0

