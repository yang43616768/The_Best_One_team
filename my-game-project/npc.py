import pygame
from setting import *
from openai import OpenAI
from typing import List,Dict

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y,image_path,name):
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
        self.dialogue_active = False
        self.dialogue_text = ''
        self.player_input = ''
        self.messages: List[Dict] = [
            {"role": "system", "content": "You are Alice,a guiding NPC in a game world.The player has just come to this world and needs your guidance.When the input involves about your identity or the setting of this game,you should tell him who you are and what you can do for him."}
        ]
        self.client = OpenAI(
            base_url='http://10.15.88.73:5001/v1',
            api_key='ollama',  # required but ignored
        )
    def draw(self,window):
        window.blit(self.image, self.rect)

    def trigger_dialogue(self,text):
        self.dialogue_active = True
        self.dialogue_text = text
        self.player_input = ''

    def draw_dialogue(self, window):
        if self.dialogue_active:
            font = pygame.font.SysFont(None, 36)
            text_surface = font.render(self.dialogue_text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(window.get_width() / 2, window.get_height() - 100))
            pygame.draw.rect(window, (0, 0, 0), text_rect.inflate(20, 20))
            window.blit(text_surface, text_rect)

            input_surface = font.render(self.player_input, True, (255, 255, 255))
            input_rect = input_surface.get_rect(center=(window.get_width() / 2, window.get_height() - 50))
            pygame.draw.rect(window, (0, 0, 0), input_rect.inflate(20, 20))
            window.blit(input_surface, input_rect)

    def handle_input(self, event):
        if self.dialogue_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # 将玩家输入的文本上传给大模型
                    self.messages.append({"role": "user", "content": self.player_input})
                    response = self.client.chat.completions.create(
                        model="llama-2-13b-chat",
                        messages=self.messages,
                    )
                    assistant_reply = response.choices[0].message.content
                    self.messages.append({"role": "assistant", "content": assistant_reply})
                    self.dialogue_text = f"NPC: {assistant_reply}"
                    self.player_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.player_input = self.player_input[:-1]
                else:
                    self.player_input += event.unicode

    def close_dialogue(self):
        self.dialogue_active = False
        self.dialogue_text = ""
        self.player_input = ""