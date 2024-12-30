import pygame
import random
import sys
from collections import EventLike as EventLike,ListenerLike as ListenerLike,GroupLike as GroupLike,Core as Core
from constants import EventCode as EventCode,StepEventBody as StepEventBody,DrawEventBody as DrawEventBody,KillEventBody as KillEventBody

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))