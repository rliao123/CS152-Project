import pygame
from pygame.locals import *
from .PlayerBullets import PlayerBullets
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("CS152-Project/images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
        self.lives = 3
        self.hidden = False
        self.hideTimer = pygame.time.get_ticks()

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if self.rect.top > 0:
            if key_pressed[K_UP] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, -1)
            if key_pressed[K_UP] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 600:
            if key_pressed[K_DOWN] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, 1)
            if key_pressed[K_DOWN] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if key_pressed[K_LEFT] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(-1, 0)
            if key_pressed[K_LEFT] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 600:
            if key_pressed[K_RIGHT] and key_pressed[K_LSHIFT]:
                self.rect.move_ip(1, 0)
            if key_pressed[K_RIGHT] and not key_pressed[K_LSHIFT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def create_bullet(self):
        # create bullet from top center of sprite
        return PlayerBullets(self.rect.x + 50 / 2, self.rect.y)


player1 = Player()


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 33 * i
        img_rect.y = y
        surf.blit(img, img_rect)


