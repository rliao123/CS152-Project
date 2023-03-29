import pygame
from pygame.locals import *
import random


class PlayerBullets(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.image.load("CS152-Project/images/player bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

    def update(self):
        self.rect.move_ip(0, -5)
        if self.rect.top < 0:
            self.kill()
