import pygame
from CharacterObject.Enemy import Enemy

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

gameIsRunning = True

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    # Draw scene
    screen.fill((248, 248, 248))
    enemy_group.draw(screen)

    enemy.pattern1()

    # Update the screen at 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Quit when game loop ends
pygame.quit()
