import pygame
from pygame.locals import *
import random

pygame.init()

BLACK = (0, 0, 0)

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

clock = pygame.time.Clock()


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
        return PlayerBullet(self.rect.x + 50 / 2, self.rect.y)


player1 = Player()


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.image = pygame.image.load("player bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (posX, posY)

    def update(self):
        self.rect.move_ip(0, -5)
        if self.rect.top < 0:
            self.kill()


pbGroup = pygame.sprite.Group()

heart = pygame.image.load("heart.png")


def drawLives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 33 * i
        img_rect.y = y
        surf.blit(img, img_rect)


gameIsRunning = True

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pbGroup.add(player1.createBullet())

    player1.update()
    pbGroup.update()
    screen.fill(BLACK)
    player1.draw(screen)
    pbGroup.draw(screen)

    drawLives(screen, 500, 5, player1.lives, heart)
    # Update the screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

# Quit when game loop ends
pygame.quit()

print("hello")
print("bye")
