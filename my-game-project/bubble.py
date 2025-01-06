
import pygame

class Bubble:
    def __init__(self, npc):
        self.npc = npc
        self.font = pygame.font.Font(None, 24)
        self.surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        self.surface.fill((255, 255, 255, 200))  # 半透明白色背景
        self.image = self.surface
        self.rect = self.surface.get_rect()
        self.update_text()

    def update_text(self):
        self.surface.fill((255, 255, 255, 200))  # 重新填充背景，以防止文字重叠
        self.text_surface = self.font.render(self.npc.bubble_texts[self.npc.current_bubble_index], True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(100, 25))
        self.surface.blit(self.text_surface, self.text_rect)
        self.image = self.surface
        self.rect.midbottom = (self.npc.rect.centerx, self.npc.rect.top - 10)
