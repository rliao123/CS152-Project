import pygame


class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/player bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y


