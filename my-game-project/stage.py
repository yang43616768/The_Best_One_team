import pygame
import sys
from setting import *
from player import *
from wall import *
from SceneManager import *
from npc import *

def draw_screen(window, background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()

def stage0(window):
    pygame.display.set_caption("Game Start")
    draw_screen(window,r".\assets\images\grass.jpg")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def stage1(window):
    player = Player(150,150)
    walls = pygame.sprite.Group()
    walls.add(Wall(100,100,2,2))
    npc1 = NPC(200,200,NpcSettings.photopath1_1,'Alice',{"role": "system", "content": NpcSettings.Task_Alice},NpcSettings.items1,NpcSettings.photopath1_2)
    npcs = [npc1]

    pygame.display.set_caption("Learn To Start")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render()
    pygame.display.flip()


    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for npc in npcs:
                        npc.close_dialogue()
                        npc.buy_active = False
                else:
                    for npc in npcs:
                        npc.handle_input(event,player)
            player.update(walls, any(npc.dialogue_active for npc in npcs),any(npc.buy_active for npc in npcs))

            window.fill((0, 0, 0))

            scene_manager.update_camera(player)  # 更新摄像机位置
            scene_manager.render()
            scene_manager.location(player)
            scene_manager.location(walls)
            for npc in npcs:
                scene_manager.location(npc)

            pygame.display.flip()

