import pygame
from pygame.locals import *
import random
from CharacterObject.Player import Player, drawLives

pygame.init()

BLACK = (0, 0, 0)

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

player1 = Player()
pbGroup = pygame.sprite.Group()
heart = pygame.image.load("heart.png")

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
