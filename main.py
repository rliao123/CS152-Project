import pygame
from CharacterObject.Enemy import Enemy
from pygame.locals import *
import random
from CharacterObject.Player import Player, drawLives

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Init enemy instance
enemy = Enemy(50, 50, 300, 150, 100000)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

player1 = Player()
pbGroup = pygame.sprite.Group()
heart = pygame.image.load("CS152-Project/images/heart.png")

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
    screen.fill((248, 248, 248))
    player1.draw(screen)
    pbGroup.draw(screen)
    enemy_group.draw(screen)
    enemy.pattern1()

    drawLives(screen, 500, 5, player1.lives, heart)

    # Update the screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Quit when game loop ends
pygame.quit()
