import pygame
from setting import *
from openai import OpenAI
from typing import List,Dict
import sys
from bubble import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y,name):
        super().__init__()
        self.name = str(name[8])
        self.image = pygame.image.load(name[2])
        self.image = pygame.transform.scale(
            self.image, (PlayerSettings.playerWidth, PlayerSettings.playerHeight)
        )
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.dialogue_font_size = 30
        self.dialogue_active = False
        self.quest_active = False
        self.buy_active = False
        self.fight_active = False
        self.dialogue_text = ''
        self.player_input = ''
        self.messages: List[Dict] = [name[0]]
        self.dialogue_history: List[str] = []
        self.client = OpenAI(
            base_url='http://10.15.88.73:5001/v1',
            api_key='ollama',  # required but ignored
        )
        self.dialogue_bg = pygame.image.load(name[3]) if name[3] else None
        self.items = name[1]  # 示例物品及其价格
        self.defeated = False
        self.round = 0
        self.damage_to_npc = 0
        self.damage_to_player = 0
        self.key_counts = {
            pygame.K_e: 0,
            pygame.K_q: 0
        }
        self.reward = name[4]       #战斗掉落物
        self.currency = name[5]     #战斗赏金
        self.health = name[6]       #血量
        self.attack_list = name[7]  #攻击意图
        self.attack = self.attack_list[0]
        self.player_health = 100
        self.attack_image = pygame.image.load(r".\assets\images\attack.png")
        self.defence_image = pygame.image.load(r".\assets\images\defence.png")
        self.attack_image = pygame.transform.scale(self.attack_image, (34, 45))
        self.defence_image = pygame.transform.scale(self.defence_image, (34, 45))
        self.bubble_text1 = name[9][0]
        self.bubble_text2 = name[9][1]
        self.bubble_text3 = name[9][2]
        self.scroll_offset = 0
        self.bubble_texts = [self.bubble_text1,self.bubble_text2,self.bubble_text3]  # 气泡显示的文本列表
        self.current_bubble_index = 0
        self.last_bubble_switch_frame = 0  # 上次切换气泡的时间
        self.bubble = Bubble(self)
        self.i = name[10]
        self.bgm_position = 0

    def draw(self,window):
        window.blit(self.image, self.rect)


    def draw_dialogue(self, window):
        if self.dialogue_active:
            if self.dialogue_bg:
                # 获取窗口和背景图像的尺寸
                window_width, window_height = window.get_size()
                bg_width, bg_height = self.dialogue_bg.get_size()

                # 计算缩放比例，保持原始比例
                scale = min(window_width / bg_width, window_height / bg_height)
                new_width = int(bg_width * scale)
                new_height = int(bg_height * scale)

                # 缩放背景图像
                bg_surface = pygame.transform.scale(self.dialogue_bg, (new_width, new_height))

                # 计算背景图像的位置，使其居中
                bg_x = (window_width - new_width) // 2
                bg_y = (window_height - new_height) // 2

                window.blit(bg_surface, (bg_x, bg_y))

            font = pygame.font.SysFont(None, self.dialogue_font_size)
            y_offset = 50-self.scroll_offset  # 从顶部开始绘制
            for i in range(0, len(self.dialogue_history), 2):
                if i < len(self.dialogue_history):
                    question_surface = font.render(self.dialogue_history[i], True, (255, 255, 255))
                    question_rect = question_surface.get_rect(topleft=(50, y_offset))
                    window.blit(question_surface, question_rect)
                    y_offset += 40

                if i + 1 < len(self.dialogue_history):
                    answer_surface = font.render(self.dialogue_history[i + 1], True, (255, 255, 255))
                    answer_rect = answer_surface.get_rect(topleft=(50, y_offset))
                    window.blit(answer_surface, answer_rect)
                    y_offset += 40

            input_surface = font.render(self.player_input, True, (255, 255, 255))
            input_rect = input_surface.get_rect(center=(window.get_width() / 2, window.get_height() - 50))
            
            # 创建一个透明背景的表面
            background_surface = pygame.Surface(input_rect.size, pygame.SRCALPHA)
            background_surface.fill((0, 0, 0, 0))  # 透明背景
            
            window.blit(background_surface, input_rect.topleft)
            window.blit(input_surface, input_rect)

            # 绘制 NPC 名字，使用更大的字体
            name_font = pygame.font.SysFont(None, 108)  # 更大的字体大小
            name_surface = name_font.render(self.name, True, (255, 255, 255))
            name_rect = name_surface.get_rect(topright=(window_width - 320, 320))
            window.blit(name_surface, name_rect)

    def handle_input(self, event,player):
        if self.dialogue_active:
            #对话窗口交互
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.messages.append({"role": "user", "content": self.player_input})
                    response = self.client.chat.completions.create(
                        model="llama3.2",
                        messages=self.messages,
                    )
                    assistant_reply = response.choices[0].message.content
                    self.messages.append({"role": "assistant", "content": assistant_reply})
                    self.dialogue_history.append(f"Player: {self.player_input}")
                    self.dialogue_history.append(f"NPC: {assistant_reply}")
                    self.player_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.player_input = self.player_input[:-1]

                elif event.key == pygame.K_ESCAPE:
                    self.dialogue_active = False
                elif event.key == pygame.K_PAGEDOWN:
                    self.scroll_offset += 30
                elif event.key == pygame.K_PAGEUP:
                    self.scroll_offset = max(self.scroll_offset - 30, 0)

                else:
                    self.player_input += event.unicode
        elif self.buy_active:
            #商店窗口交互
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b:
                    self.buy_active = False  # 关闭购买界面
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    item_index = event.key - pygame.K_1
                    if item_index < len(self.items):
                        item_name, item_price = self.items[item_index]
                        if player.currency >= item_price:
                            player.currency -= item_price
                            player.add_item(item_name)
                            self.items.pop(item_index)  # 从商店中移除该物品
        elif self.fight_active:
            #战斗窗口交互
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.fight_active = False
                elif event.key in [pygame.K_q,pygame.K_e]:
                    if (self.key_counts[pygame.K_q] + self.key_counts[pygame.K_e]) < (player.moves-1):
                        self.key_counts[event.key] += 1  # 记录按键次数

                    elif (self.key_counts[pygame.K_q] + self.key_counts[pygame.K_e]) == (player.moves-1):
                        self.key_counts[event.key] += 1
                        self.fight_calculate(player)
                    elif (self.key_counts[pygame.K_q] + self.key_counts[pygame.K_e]) == player.moves:
                        self.round += 1
                        self.key_counts[pygame.K_q] = 0
                        self.key_counts[pygame.K_e] = 0
                    
        elif not self.buy_active and not self.dialogue_active and not self.fight_active:
            distance = pygame.math.Vector2(self.rect.center).distance_to(player.rect.center)
            if distance <= 80:
                self.quest_active = True
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.dialogue_active = True
                    elif event.key == pygame.K_b:
                        self.buy_active = True
                    elif event.key == pygame.K_f and not self.defeated:
                        self.fight_active = True
                        self.bgm_position = pygame.mixer.music.get_pos() / 1000.0  # 获取当前背景音乐的播放位置（秒）
                        pygame.mixer.music.load(r".\assets\bgm\boss.mp3")
                        pygame.mixer.music.play(-1)           
            elif distance > 80:
                self.quest_active = False
    def close_dialogue(self):
        self.dialogue_active = False
        self.dialogue_text = ""
        self.player_input = ""
        self.dialogue_history = []

    def switch_bubble(self):
            current_frame = pygame.time.get_ticks() // (1000 // 60)  # 获取当前帧数
            if current_frame - self.last_bubble_switch_frame > 120:  # 每隔120帧切换一次气泡
                self.current_bubble_index = (self.current_bubble_index + 1) % len(self.bubble_texts)
                self.last_bubble_switch_frame = current_frame
                self.bubble.update_text()
    def draw_buy(self,window):
        # 绘制购买界面的背景
        buy_bg = pygame.Surface((600, 300))
        buy_bg.fill((0, 0, 0))  # 黑色背景
        buy_bg.set_alpha(200)  # 半透明
        window.blit(buy_bg, (window.get_width() // 2 - 300, window.get_height() // 2 - 150))

        # 绘制购买界面的文本
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render("Buy Items", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 100))
        window.blit(text_surface, text_rect)


        # 绘制物品列表
        for i, (item, price) in enumerate(self.items):
            item_surface = font.render(f"{i+1}. {item} - {price} currency", True, (255, 255, 255))
            item_rect = item_surface.get_rect(topleft=(window.get_width() // 2 - 200, window.get_height() // 2 - 50 + i * 40))
            window.blit(item_surface, item_rect)


    def fight_calculate(self,player):
        self.attack = self.attack_list[self.round%len(self.attack_list)]
        self.player_health = player.health
        self.damage_to_npc += self.key_counts[pygame.K_e] * player.attack
        if self.attack-self.key_counts[pygame.K_q] *player.defense >= 0:
            self.damage_to_player += self.attack-self.key_counts[pygame.K_q] *player.defense 



        if player.health - self.damage_to_player <= 0:
            self.fight_failed()
        elif self.health - self.damage_to_npc <= 0:
            self.fight_succeeded(player)

    def draw_cards(self, window, y_offset):
        # 绘制攻击牌
        for i in range(self.key_counts[pygame.K_e]):
            window.blit(self.attack_image, (50 + i * 60, y_offset))

        # 绘制防御牌
        for i in range(self.key_counts[pygame.K_q]):
            window.blit(self.defence_image, (50 + i * 60, y_offset + 60))


    def fight_failed(self):
        self.round = 0
        self.damage_to_npc = 0
        self.damage_to_player = 0
        self.fight_active = False
        self.key_counts[pygame.K_q] = 0
        self.key_counts[pygame.K_e] = 0
        if self.i == 1:
            pygame.mixer.music.load(r".\assets\bgm\StartMenu.mp3")
        elif self.i == 2:
            pygame.mixer.music.load(r".\assets\bgm\city.mp3")
        elif self.i == 3:
            pygame.mixer.music.load(r".\assets\bgm\HisTheme.mp3")
        pygame.mixer.music.play(-1, start=self.bgm_position)  # 从记录的位置继续播放
    def fight_succeeded(self,player):
        self.round = 0
        self.damage_to_npc = 0
        self.damage_to_player = 0
        self.fight_active = False
        self.defeated = True
        player.add_item(self.reward)
        player.currency += self.currency
        if self.i == 1:
            pygame.mixer.music.load(r".\assets\bgm\StartMenu.mp3")
        elif self.i == 2:
            pygame.mixer.music.load(r".\assets\bgm\city.mp3")
        elif self.i == 3:
            pygame.mixer.music.load(r".\assets\bgm\HisTheme.mp3")
        pygame.mixer.music.play(-1)

    def draw_fight(self,window):

        font = pygame.font.Font(None, 36)
        window.fill((0, 0, 0))  # 清空窗口

        # 绘制玩家图像和npc图像
        player_image = pygame.image.load(Gamepath.player)
        player_image_scaled = pygame.transform.scale(player_image, (250, 300))

        player_image_rect = player_image_scaled.get_rect(topleft=(50, 200))
        window.blit(player_image_scaled, player_image_rect)

        npc_fight_image = pygame.transform.scale(self.image, (250, 300))
        npc_image_rect = npc_fight_image.get_rect(topright=(window.get_width() - 50, 200))
        window.blit(npc_fight_image, npc_image_rect)

        # 绘制玩家血量
        player_health_text = font.render(f"Player Health: {self.player_health - self.damage_to_player}", True, (255, 255, 255))
        player_health_rect = player_health_text.get_rect(midtop=(player_image_rect.centerx, player_image_rect.bottom + 10))
        window.blit(player_health_text, player_health_rect)
        self.draw_health_bar(window, player_image_rect.centerx, player_image_rect.bottom + 40, self.player_health-self.damage_to_player, self.player_health)
        
        # 绘制NPC血量
        npc_health_text = font.render(f"NPC Health: {self.health - self.damage_to_npc}", True, (255, 255, 255))
        npc_health_rect = npc_health_text.get_rect(midtop=(npc_image_rect.centerx, npc_image_rect.bottom + 10))
        window.blit(npc_health_text, npc_health_rect)
        self.draw_health_bar(window, npc_image_rect.centerx, npc_image_rect.bottom + 40, self.health-self.damage_to_npc, self.health)

        # 绘制回合数
        round_text = font.render(f"Round: {self.round}", True, (255, 255, 255))
        round_rect = round_text.get_rect(center=(window.get_width() / 2, 50))
        window.blit(round_text, round_rect)

        self.draw_cards(window, player_image_rect.bottom + 70)

        # 绘制 NPC 本回合的攻击意图
        current_attack = self.attack_list[self.round % len(self.attack_list)]
        font = pygame.font.SysFont(None, 36)
        attack_text = font.render(f"NPC Attack Intent: {current_attack}", True, (255, 255, 255))
        attack_rect = attack_text.get_rect(midtop=(npc_image_rect.centerx,npc_image_rect.bottom + 90))
        window.blit(attack_text, attack_rect)

        # 添加战斗提示文字
        action_font = pygame.font.SysFont(None, 36)
        defend_text = action_font.render("Press Q to Defend", True, (255, 255, 255))
        attack_text = action_font.render("Press E to Attack", True, (255, 255, 255))
        defend_rect = defend_text.get_rect(center=(window.get_width() // 2, window.get_height() - 100))
        attack_rect = attack_text.get_rect(center=(window.get_width() // 2, window.get_height() - 60))
        window.blit(defend_text, defend_rect)
        window.blit(attack_text, attack_rect)

    def draw_health_bar(self, window, x, y, current_health, max_health):
        bar_width = 200
        bar_height = 20
        health_ratio = current_health / max_health

        # 绘制白色背景条
        pygame.draw.rect(window, (255, 255, 255), (x - bar_width // 2, y, bar_width, bar_height))

        # 绘制红色血条
        pygame.draw.rect(window, (255, 0, 0), (x - bar_width // 2, y, bar_width * health_ratio, bar_height))

