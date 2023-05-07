import pygame
from pygame.locals import *
from .PlayerBullets import PlayerBullets
import random


class Player(pygame.sprite.Sprite):
    """A class used to represent Player"""
    def __init__(self):
        """Initializes Player object"""
        super().__init__()
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
        self.hitbox = Rect(0, 0, 6, 6)  # 6x6 hitbox
        self.hitbox.center = self.rect.center
        self.lives = 3
        self.hidden = False
        self.hideTimer = pygame.time.get_ticks()

    def update(self):
        """Update and move the player's rect according to keys pressed and set player's hitbox
        Does not allow player to move outside of screen's borders
        Player's coordinates change a smaller amount if left shift key and arrow key are clicked simultaneously
        """

        key_pressed = pygame.key.get_pressed()

        if self.rect.top > 0:
            if key_pressed[K_UP] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, -2)
            if key_pressed[K_UP] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 600:
            if key_pressed[K_DOWN] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, 2)
            if key_pressed[K_DOWN] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if key_pressed[K_LEFT] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(-2, 0)
            if key_pressed[K_LEFT] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 600:
            if key_pressed[K_RIGHT] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(2, 0)
            if key_pressed[K_RIGHT] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(5, 0)

        self.hitbox.center = self.rect.center

    def draw(self, surface):
        """Draw player and player's hitbox on surface"""
        surface.blit(pygame.Surface([6, 6]), self.hitbox)
        surface.blit(self.image, self.rect)

    def create_bullet(self):
        """Create player bullet with top center of sprite coordinates"""

        return PlayerBullets(self.rect.x + 50 / 2, self.rect.y)


def draw_lives(surf, x, y, lives, img):
    """Draw life icons according to amount of lives player has

    surf -- surface to display image on
    x -- x coordinate to draw lives
    y -- y coordinate to draw lives
    lives -- amount of lives player has
    img -- icon to represent the lives
    """

    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 33 * i
        img_rect.y = y
        surf.blit(img, img_rect)


