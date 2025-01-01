import pygame
from setting import *
from openai import OpenAI
from typing import List,Dict

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y,image_path,name,setting,bg_path=None):
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
        self.dialogue_text = ''
        self.player_input = ''
        self.messages: List[Dict] = [setting]
        self.dialogue_history: List[str] = []
        self.scroll_offset = 0
        self.client = OpenAI(
            base_url='http://10.15.88.73:5001/v1',
            api_key='ollama',  # required but ignored
        )
        self.dialogue_bg = pygame.image.load(bg_path) if bg_path else None
    def draw(self,window):
        window.blit(self.image, self.rect)

    def trigger_dialogue(self,text):
        self.dialogue_active = True
        self.dialogue_text = text
        self.player_input = ''

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

    def handle_input(self, event):
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
                else:
                    self.player_input += event.unicode

    def close_dialogue(self):
        self.dialogue_active = False
        self.dialogue_text = ""
        self.player_input = ""
        self.dialogue_history = []