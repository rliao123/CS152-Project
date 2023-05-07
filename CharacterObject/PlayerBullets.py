import pygame
from pygame.locals import *
import random


class PlayerBullets(pygame.sprite.Sprite):
    """A class used to represent Player Bullet"""
    def __init__(self, posX, posY):
        """Initializes Player Bullet object
        posX -- center x coordinate of player bullet
        posY -- center y coordinate of player bullet
        """

        super().__init__()
        self.image = pygame.image.load("images/player bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

    def update(self):
        """Moves player bullet up the screen"""

        self.rect.move_ip(0, -5)
        # destroy bullet when it goes outside the screen's borders
        if self.rect.top < 0:
            self.kill()
