import pygame
pygame.init()

BLACK = (0, 0, 0)

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

clock = pygame.time.Clock()

gameIsRunning = True

while gameIsRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    screen.fill(BLACK)

    # Update the screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

# Quit when game loop ends
pygame.quit()

print("hello")
print("bye")