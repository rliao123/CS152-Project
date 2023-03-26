import pygame
from pygame.locals import *
from .PlayerBullets import PlayerBullets
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
        self.lives = 3
        self.hidden = False
        self.hideTimer = pygame.time.get_ticks()

    def update(self):
        keyPressed = pygame.key.get_pressed()

        if self.rect.top > 0:
            if keyPressed[K_UP] and keyPressed[K_LSHIFT]:
                self.rect.move_ip(0, -1)
            if keyPressed[K_UP] and not keyPressed[K_LSHIFT]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 600:
            if keyPressed[K_DOWN] and keyPressed[K_LSHIFT]:
                self.rect.move_ip(0, 1)
            if keyPressed[K_DOWN] and not keyPressed[K_LSHIFT]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if keyPressed[K_LEFT] and keyPressed[K_LSHIFT]:
                self.rect.move_ip(-1, 0)
            if keyPressed[K_LEFT] and not keyPressed[K_LSHIFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 600:
            if keyPressed[K_RIGHT] and keyPressed[K_LSHIFT]:
                self.rect.move_ip(1, 0)
            if keyPressed[K_RIGHT] and not keyPressed[K_LSHIFT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def createBullet(self):
        # create bullet from top center of sprite
        return PlayerBullets(self.rect.x + 50 / 2, self.rect.y)


player1 = Player()


def drawLives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 33 * i
        img_rect.y = y
        surf.blit(img, img_rect)


