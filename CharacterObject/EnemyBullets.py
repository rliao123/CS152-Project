import pygame
import math


class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((100, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.angle = angle

    def update(self):
        self.rect.x += 5 * math.cos(math.radians(self.angle))
        self.rect.y += 5 * math.sin(math.radians(self.angle))
        if self.rect.top < 0 or self.rect.bottom > 600 or self.rect.right > 600 or self.rect.left < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
