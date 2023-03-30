import pygame
from CharacterObject.Enemy import Enemy, draw_health_bar
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

path_pattern_1 = [(300, 200)]
path_pattern_2 = [(100, 150), (300, 150), (500, 150), (300, 150)]
path_pattern_3 = [(100, 100), (500, 200), (500, 100), (100, 200)]
path_pattern_4 = [(300, 200)]
path_pattern_5 = [(100, 100), (500, 200), (500, 100), (100, 200)]

player1 = Player()
pbGroup = pygame.sprite.Group()
heart = pygame.image.load("images/heart.png")

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
    screen.fill((0, 0, 0))
    player1.draw(screen)
    pbGroup.draw(screen)
    enemy_group.draw(screen)

    if enemy.health >= enemy.max_health * (4/5):
        enemy.move_in_pattern(path_pattern_1, 2)
    elif enemy.health >= enemy.max_health * (3/5):
        enemy.move_in_pattern(path_pattern_2, 2)
    elif enemy.health >= enemy.max_health * (2/5):
        enemy.move_in_pattern(path_pattern_3, 5)
    elif enemy.health >= enemy.max_health * (1/5):
        enemy.move_in_pattern(path_pattern_4, 5)
    elif enemy.health > enemy.max_health * (0/5):
        enemy.move_in_pattern(path_pattern_5, 10)
    elif enemy.health == 0:
        enemy.kill()

    drawLives(screen, 500, 550, player1.lives, heart)
    draw_health_bar(screen, 300, 20, enemy.health, enemy.max_health)

    # Update the screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Quit when game loop ends
pygame.quit()
