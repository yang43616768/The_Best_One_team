import pygame
import sys
from setting import *
from player import *
from wall import *
from SceneManager import *
from npc import *
from portal import *
from transparent import *


def draw_screen(window, background_path):
    background = pygame.image.load(background_path)
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WindowsSettings.width / 2, WindowsSettings.height / 2))
    window.blit(text, text_rect)
    pygame.display.flip()

def stage_common(npcs,player,walls,transparents,portal,scene_manager,window,i):
    waiting = True
    while waiting:
        for npc in npcs:
            npc.player_health = player.health
            npc.switch_bubble()
            scene_manager.location(npc.bubble,npcs)
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    for npc in npcs:
                        npc.close_dialogue()
                        npc.buy_active = False
                    player.bag_active = False
                elif event.key == pygame.K_i and not any(npc.dialogue_active for npc in npcs):  # 按下i键打开背包
                    player.bag_active = not player.bag_active
                elif event.key == pygame.K_PAGEDOWN or event.key == pygame.K_PAGEUP:
                    if event.key == pygame.K_PAGEUP:  # 向上
                        player.scroll_offset = max(player.scroll_offset - 30, 0)
                    elif event.key == pygame.K_PAGEDOWN:  # 向下
                        player.scroll_offset += 30
                else:
                    for npc in npcs:
                        npc.handle_input(event,player)
            player.update(walls, any(npc.dialogue_active for npc in npcs),any(npc.buy_active for npc in npcs),scene_manager)
            for transparent in transparents:
                transparent.check_transparent(player)

            window.fill((0, 0, 0))

            scene_manager.update_camera(player)  # 更新摄像机位置
            if i == 1:
                scene_manager.render1(npcs)
            if i == 2:
                scene_manager.render2(npcs)
            if i == 3:
                scene_manager.render3(npcs)
            scene_manager.location(player,npcs)
            scene_manager.location(walls,npcs)
            for npc in npcs:
                scene_manager.location(npc,npcs)
            scene_manager.location(portal,npcs)
            for transparent in transparents:
                scene_manager.location(transparent,npcs)
            player.show_inventory(scene_manager.window)
            portal.check_telepotation(player,event,npcs)
            player.draw_item_message(window)
            pygame.display.flip()
            if portal.tp_succeed:
                waiting = False

def stage0(window):
    pygame.display.set_caption("Game Start")
    pygame.mixer.music.load(r".\assets\bgm\LightningMoment.mp3")
    pygame.mixer.music.play(-1)  # 循环播放
    draw_screen(window,r".\assets\images\grass.jpg")
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def stage1(window,player):

    pygame.mixer.music.load(r".\assets\bgm\StartMenu.mp3")
    pygame.mixer.music.play(-1)  # 循环播放

    walls = pygame.sprite.Group()


    npc1 = NPC(575,875,NpcSettings.Lilia)
    npc2 = NPC(275,225,NpcSettings.Berries)
    npc3 = NPC(275,1525,NpcSettings.Nyakori)
    npc4 = NPC(1375,875,NpcSettings.Eliza)
    npc5 = NPC(2700,875,NpcSettings.Sakura)
    npcs = [npc1,npc2,npc3,npc4,npc5]
    portal = Portal(r".\assets\images\portal.png",["The Legendary Sword","The Legendary Shield","The Legendary Armor","The philosopher's stone"], 2850, 875)
 ##
    walls.add(Wall(0,490,800,20))
    walls.add(Wall(0,1290,800,20))
    walls.add(Wall(780,510,20,290))
    walls.add(Wall(780,1000,20,290))
    walls.add(Wall(1090,300,20,1200))

    walls.add(Wall(1390,0,20,700))
    walls.add(Wall(1390,1100,20,700))
    walls.add(Wall(2090,0,20,700))
    walls.add(Wall(2090,1100,20,700))
    walls.add(Wall(1410,680,680,20))
    walls.add(Wall(1410,1100,680,20))

    walls.add(Wall(2110,390,890,20))
    walls.add(Wall(2110,1390,890,20))


    npcs = [npc1,npc2,npc3,npc4,npc5]
    
    transparent_roof1 = Transparent(r".\assets\images\roof.png",0,500,800,800)
    transparent_roof2 = Transparent(r".\assets\images\roof.png",0,0,600,500)
    transparent_roof3 = Transparent(r".\assets\images\roof.png",0,1300,600,500)
    transparent_roof4 = Transparent(r".\assets\images\roof.png",1400,0,700,700)
    transparent_roof5 = Transparent(r".\assets\images\roof.png",1400,1100,700,700)
    transparent_roof6 = Transparent(r".\assets\images\roof.png",2100,0,900,400)
    transparent_roof7 = Transparent(r".\assets\images\roof.png",2100,1400,900,400)

    transparents = [transparent_roof1,transparent_roof2,transparent_roof3,transparent_roof4,transparent_roof5,transparent_roof6,transparent_roof7]

    pygame.display.set_caption("Learn To Start")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)

    # 全物品指令

    for item in Item_List.keys:   
        player.add_item(item)

    scene_manager.render1(npcs)
    stage_common(npcs,player,walls,transparents,portal,scene_manager,window,1)


def stage2(window,player):

    pygame.mixer.music.load(r".\assets\bgm\city.mp3")
    pygame.mixer.music.play(-1)  # 循环播放

    # player.rect.x = 1475
    # player.rect.y = 475
    player.rect.x = 2800
    player.rect.y = 700

    walls = pygame.sprite.Group()
    walls.add(Wall(1110,390,780,20))
    walls.add(Wall(1090,300,20,700))
    walls.add(Wall(1890,390,20,610))
    walls.add(Wall(1110,980,290,20))
    walls.add(Wall(1600,980,290,20))
    walls.add(Wall(1910,890,1090,20))
    walls.add(Wall(400,300,690,20))
    walls.add(Wall(400,320,20,580))

    walls.add(Wall(0,1300,2400,20))
    walls.add(Wall(2600,1300,400,20))
    walls.add(Wall(1490,1300,20,500))
    walls.add(Wall(790,600,20,700))



    npc1 = NPC(1475,800,NpcSettings.Theia)
    npc2 = NPC(1600,1525,NpcSettings.Lianne)
    npc3 = NPC(375,1075,NpcSettings.Irin)
    npc4 = NPC(1750,175,NpcSettings.Irin_Evil)
    npcs = [npc1,npc2,npc3,npc4]
    portal = Portal(r".\assets\images\portal.png",["The Evil Black Mandala","The Container"], 2800,700)
    transparent_roof1 = Transparent(r".\assets\images\roof.png",1100,400,800,600)
    transparent_roof2 = Transparent(r".\assets\images\roof.png",0,1300,750,500)
    transparent_roof3 = Transparent(r".\assets\images\roof.png",750,1300,750,500)
    transparent_roof4 = Transparent(r".\assets\images\roof.png",1500,1300,1500,500)
    transparent_roof5 = Transparent(r".\assets\images\roof.png",0,900,800,400)

    transparents = [transparent_roof1,transparent_roof2,transparent_roof3,transparent_roof4,transparent_roof5]

    pygame.display.set_caption("We are getting deeper...into the Truth")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render2(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window,2)

def stage3(window,player):

    pygame.mixer.music.load(r".\assets\bgm\HisTheme.mp3")
    pygame.mixer.music.play(-1)  # 循环播放

    player.rect.x = 1600
    player.rect.y = 900
    walls = pygame.sprite.Group()
    walls.add(Wall(0,390,800,20))
    walls.add(Wall(0,1390,800,20))
    walls.add(Wall(780,410,20,390))
    walls.add(Wall(780,1000,20,390))

    walls.add(Wall(1980,290,1020,20))
    walls.add(Wall(1980,1490,1020,20))
    walls.add(Wall(2000,310,20,490))
    walls.add(Wall(2000,1000,20,490))

    walls.add(Wall(800,590,1200,20))
    walls.add(Wall(800,1210,1200,20))

    npc1 = NPC(575,875,NpcSettings.Drakura)
    npc2 = NPC(2475,875,NpcSettings.Nyarutoru)

    npcs = [npc1,npc2]
    portal = Portal(r".\assets\images\portal.png",["The Vessel of Blood","The Bow Tie of Nyarutoru"], 2850, 875)
    transparent_roof1 = Transparent(r".\assets\images\roof.png",0,0,800,400)
    transparent_roof2 = Transparent(r".\assets\images\roof.png",0,1400,800,400)
    transparent_roof3 = Transparent(r".\assets\images\roof.png",800,0,1200,600)
    transparent_roof4 = Transparent(r".\assets\images\roof.png",800,1200,1200,600)
    transparent_roof5 = Transparent(r".\assets\images\roof.png",2000,0,1000,300)
    transparent_roof6 = Transparent(r".\assets\images\roof.png",2000,1500,1000,300)
    transparent_roof7 = Transparent(r".\assets\images\roof.png",0,400,800,1000)
    transparents = [transparent_roof1,transparent_roof2,transparent_roof3,transparent_roof4,transparent_roof5,transparent_roof6,transparent_roof7]

    pygame.display.set_caption("The Final Chapter.")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render3(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window,3)
