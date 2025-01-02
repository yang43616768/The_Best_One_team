import pygame
from setting import *
from openai import OpenAI
from typing import List,Dict

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y,image_path,name,setting,items,bg_path=None):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            self.image, (PlayerSettings.playerWidth, PlayerSettings.playerHeight)
        )
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.name = name
        self.dialogue_font_size = 36
        self.dialogue_active = False
        self.buy_active = False
        self.dialogue_text = ''
        self.player_input = ''
        self.messages: List[Dict] = [setting]
        self.dialogue_history: List[str] = []
        self.client = OpenAI(
            base_url='http://10.15.88.73:5001/v1',
            api_key='ollama',  # required but ignored
        )
        self.dialogue_bg = pygame.image.load(bg_path) if bg_path else None
        self.items = items  # 示例物品及其价格
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
            y_offset = 50  # 从顶部开始绘制
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

    def handle_input(self, event,player):
        if self.dialogue_active:
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
                else:
                    self.player_input += event.unicode
        elif self.buy_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.buy_active = False  # 关闭购买界面
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    item_index = event.key - pygame.K_1
                    if item_index < len(self.items):
                        item_name, item_price = self.items[item_index]
                        if player.currency >= item_price:
                            player.currency -= item_price
                            player.inventory.append(item_name)
                            self.items.pop(item_index)  # 从商店中移除该物品

        elif not self.buy_active and not self.dialogue_active:
            distance = pygame.math.Vector2(self.rect.center).distance_to(player.rect.center)
            if event.type == pygame.KEYDOWN and distance <= 40:
                if event.key == pygame.K_e:
                    self.dialogue_active = True
                elif event.key == pygame.K_b:
                    self.buy_active = True
    def close_dialogue(self):
        self.dialogue_active = False
        self.dialogue_text = ""
        self.player_input = ""
        self.dialogue_history = []



    def draw_buy(self,window):
        # 绘制购买界面的背景
        buy_bg = pygame.Surface((400, 300))
        buy_bg.fill((0, 0, 0))  # 黑色背景
        buy_bg.set_alpha(200)  # 半透明
        window.blit(buy_bg, (window.get_width() // 2 - 200, window.get_height() // 2 - 150))

        # 绘制购买界面的文本
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render("Buy Items", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 100))
        window.blit(text_surface, text_rect)


        # 绘制物品列表
        for i, (item, price) in enumerate(self.items):
            item_surface = font.render(f"{i+1}. {item} - {price} currency", True, (255, 255, 255))
            item_rect = item_surface.get_rect(topleft=(window.get_width() // 2 - 150, window.get_height() // 2 - 50 + i * 40))
            window.blit(item_surface, item_rect)


    # def trigger_fight(self):
