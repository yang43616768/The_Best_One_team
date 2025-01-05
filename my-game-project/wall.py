import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # self.image = pygame.Surface([width, height])
        # self.image.fill((255, 0, 0))
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)  # 使用 SRCALPHA 以支持透明度
        self.image.fill((255, 255, 255, 128))  # 设置颜色为白色，透明度为 128 (0-255)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y)) 