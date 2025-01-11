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
            scene_manager.location(portal,npcs)
            scene_manager.location(player,npcs)
            scene_manager.location(walls,npcs)
            
            for npc in npcs:
                scene_manager.location(npc, npcs)


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


    npc1 = NPC(555,875,NpcSettings.Lilia)
    npc2 = NPC(275,225,NpcSettings.Berries)
    npc3 = NPC(275,1525,NpcSettings.Nyakori)
    npc4 = NPC(1375,855,NpcSettings.Eliza)
    npc5 = NPC(2700,855,NpcSettings.Sakura)
    npcs = [npc1,npc2,npc3,npc4,npc5]
<<<<<<< HEAD
    portal = Portal(r".\assets\images\portal.png",["The Legendary Sword","The Legendary Shield","The Legendary Armor","The philosopher's stone"], 2800, 825)
=======
    portal = Portal(r".\assets\images\portal.png",["The Legendary Sword","The Legendary Shield","The Legendary Armor","The philosopher's stone"], 2850, 775)
>>>>>>> 900bdbad248e3a38513fd68cee7a5673a1a4d03a

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

    player.rect.x = 1550
    player.rect.y = 1400
    walls = pygame.sprite.Group()
    walls.add(Wall(0,390,800,20))

    npc1 = NPC(1550,1625,NpcSettings.Drakura)
    npc2 = NPC(1550,750,NpcSettings.Nyarutoru)

    npcs = [npc1,npc2]
<<<<<<< HEAD
    portal = Portal(r".\assets\images\portal.png",["The Vessel of Blood","The Bow Tie of Nyarutoru"], 1500, 100)
=======
    portal = Portal(r".\assets\images\portal.png",["The Vessel of Blood","The Bow Tie of Nyarutoru"], 1500, 200)
>>>>>>> 900bdbad248e3a38513fd68cee7a5673a1a4d03a
    transparent_roof1 = Transparent(r".\assets\images\roof.png",0,0,0,0)

    transparents = [transparent_roof1]

    pygame.display.set_caption("The Final Chapter.")

    scene_manager = SceneManager(window)
    scene_manager.tick(30)
    scene_manager.render3(npcs)

    stage_common(npcs,player,walls,transparents,portal,scene_manager,window,3)

def stage4(window):
    pygame.mixer.music.load(r".\assets\bgm\LightningMoment.mp3")
    pygame.mixer.music.play(-1)  # 循环播放
    pygame.display.set_caption("Thanks for playing!")
    # 加载结束界面的图片
    end_images = [
        pygame.image.load(r".\assets\images\ending0.png"),
        pygame.image.load(r".\assets\images\ending1.png"),
        pygame.image.load(r".\assets\images\ending2.png"),
        pygame.image.load(r".\assets\images\ending3.png"),
        pygame.image.load(r".\assets\images\ending4.png"),
        pygame.image.load(r".\assets\images\ending5.png"),
        pygame.image.load(r".\assets\images\ending6.png"),
        pygame.image.load(r".\assets\images\ending7.png"),
        pygame.image.load(r".\assets\images\ending8.png"),
        pygame.image.load(r".\assets\images\ending9.png"),
        pygame.image.load(r".\assets\images\ending10.png")
    ]
    end_images = [pygame.transform.scale(img, (WindowsSettings.width, WindowsSettings.height)) for img in end_images]

    # 设置结束语
    end_text = "Thanks for playing!"
    font = pygame.font.SysFont(None, 72)
    text_surface = font.render(end_text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WindowsSettings.width // 2, WindowsSettings.height // 2))

    # 初始化透明度
    alpha = 0
    alpha_increment = 1  # 每帧增加的透明度值
    max_alpha = 255  # 最大透明度值

    # 初始化图片切换
    current_image_index = 0
    image_switch_time = 3000  # 每张图片显示的时间（毫秒）
    last_switch_time = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 获取当前时间
        current_time = pygame.time.get_ticks()

        # 切换图片
        if current_time - last_switch_time > image_switch_time:
            current_image_index = (current_image_index + 1) % len(end_images)
            last_switch_time = current_time

        # 绘制当前的结束界面图片
        window.blit(end_images[current_image_index], (0, 0))

        # 更新透明度
        if alpha < max_alpha:
            alpha += alpha_increment
        else:
            alpha = max_alpha

        # 创建一个带有透明度的文本表面
        text_surface.set_alpha(alpha)
        window.blit(text_surface, text_rect)

        # 更新显示
        pygame.display.flip()
        clock.tick(60)