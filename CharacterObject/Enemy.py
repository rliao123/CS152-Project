import pygame
from .EnemyBullets import EnemyBullets


class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, max_health):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health

    def update(self):
        self.rect.center = [self.x, self.y]
        return True

    def move_in_pattern(self, path, vel):
        direction = pygame.math.Vector2(path[0]) - (self.x, self.y)

        if direction.length() <= vel:
            self.x = path[0][0]
            self.y = path[0][1]
            path.append(path[0])
            path.pop(0)
        else:
            direction.scale_to_length(vel)
            new_pos = pygame.math.Vector2((self.x, self.y)) + direction
            self.x = new_pos.x
            self.y = new_pos.y
            self.update()

        cur_pos = (self.x, self.y)
        return cur_pos

    def create_bullet(self, image, angle, speed, spin_delta):
        return EnemyBullets(image, self.rect.centerx, self.rect.centery, angle, speed, spin_delta)


def draw_health_bar(surf, x, y, health, max_health):
    if health > 0:
        health_bar = pygame.Surface([(health / max_health) * 500, y / 2])
        health_bar.fill((255, 255, 0))
        health_bar_rect = health_bar.get_rect()
        health_bar_rect.center = [x, y]
        surf.blit(health_bar, health_bar_rect)
