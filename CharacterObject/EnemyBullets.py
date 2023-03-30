import pygame
import math


class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def update(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))
        if self.rect.top < 0 or self.rect.bottom > 600 or self.rect.right > 600 or self.rect.left < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
