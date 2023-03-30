import pygame
from pygame.locals import *
from .PlayerBullets import PlayerBullets
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
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
        surface.blit(pygame.Surface([6, 6]), self.hitbox)
        surface.blit(self.image, self.rect)  # move this line above the previous line to preview hitbox size

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


