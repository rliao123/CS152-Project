import pygame, sys
from CharacterObject.Enemy import Enemy, draw_health_bar
from pygame.locals import *
import random, time
from CharacterObject.Player import Player, draw_lives

pygame.init()
clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# fonts and text
font = pygame.font.SysFont("Arial", 60)
game_over = font.render("Game Over", True, (255, 255, 255))
you_win = font.render("YOU WIN!", True, (0, 255, 0))
you_lost = font.render("YOU LOST :(", True, (255, 0, 0))

# Init enemy instance
enemy = Enemy(50, 50, 300, 150, 100000)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)

path_pattern_1 = [(100, 150), (300, 150), (500, 150), (300, 150)]
path_pattern_2 = [(300, 200)]
path_pattern_3 = [(100, 100), (500, 200), (500, 100), (100, 200)]
path_pattern_4 = [(300, 200)]
path_pattern_5 = [(100, 100), (500, 200), (500, 100), (100, 200)]

player1 = Player()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
heart = pygame.image.load("CS152-Project/images/heart.png")

next_time = 0  # for time counting
gameIsRunning = True

while gameIsRunning:

    start = pygame.time.get_ticks()
    angle = 30  # angle that enemy bullets are shot

    for event in pygame.event.get():
        key_pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if key_pressed[K_z]:
            player_bullet_group.add(player1.create_bullet())

    wait = 1500  # enemy shoot bullets every 1.5 seconds
    now = pygame.time.get_ticks()
    if now > next_time:
        next_time += wait
        for i in range(12):
            angle += 30
            enemy_bullet_group.add(enemy.create_bullet(angle))

    # check for collisions between player and enemy bullets
    for enemy_bullet in enemy_bullet_group:
        if enemy_bullet.rect.colliderect(player1.rect):
            player1.lives -= 1
            enemy_bullet.kill()

    # check for collisions between enemy and player bullets
    for player_bullet in player_bullet_group:
        if player_bullet.rect.colliderect(enemy.rect):
            player_bullet.kill()
            enemy.health -= 100  # not updating the health bar

    player1.update()
    player_bullet_group.update()
    screen.fill((0, 0, 0))
    player1.draw(screen)
    player_bullet_group.draw(screen)
    enemy_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)

    if enemy.health >= enemy.max_health * (4 / 5):
        enemy.move_in_pattern(path_pattern_1, 2)
    elif enemy.health >= enemy.max_health * (3 / 5):
        enemy.move_in_pattern(path_pattern_2, 2)
    elif enemy.health >= enemy.max_health * (2 / 5):
        enemy.move_in_pattern(path_pattern_3, 5)
    elif enemy.health >= enemy.max_health * (1 / 5):
        enemy.move_in_pattern(path_pattern_4, 5)
    elif enemy.health > enemy.max_health * (0 / 5):
        enemy.move_in_pattern(path_pattern_5, 10)
    elif enemy.health == 0:
        enemy.kill()
        screen.fill((0, 0, 0))
        screen.blit(game_over, (145, 200))
        screen.blit(you_win, (160, 250))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        sys.exit()
        print("YOU WIN")

    # enemy.health -= 100

    draw_lives(screen, 500, 550, player1.lives, heart)
    draw_health_bar(screen, 300, 20, enemy.health, enemy.max_health)

    # game over if player has no more lives
    if player1.lives == 0:
        screen.fill((0, 0, 0))
        screen.blit(game_over, (145, 200))
        screen.blit(you_lost, (135, 250))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        sys.exit()

    # Update the screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Quit when game loop ends
pygame.quit()
