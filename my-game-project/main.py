import pygame
import random
import sys
from setting import *
from player import *

def draw_screen(window,background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()


def main():
    pygame.init()
    window = pygame.display.set_mode((WindowsSettings.width, WindowsSettings.height))

    # Stage 0 - Start Screen
    pygame.display.set_caption("Game Start")
    draw_screen(window,r".\assets\images\grass.png")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    player = Player(100,100)
    walls = []
    # Stage 1 - Teaching Section
    pygame.display.set_caption("Learn To Start")
    #......进行教学关背景渲染与墙体生成，并将npc和玩家位置初始化
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        Player.update(walls)
if __name__ == "__main__":
    main()