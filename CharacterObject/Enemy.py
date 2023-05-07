import pygame
from .EnemyBullets import EnemyBullets


class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, h, x, y, max_health):
        """Constructor for Enemy class
        """

        super().__init__()
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health

    def update(self):
        """Updates the state of the rect/enemy-sprite to the Enemy object's current position
        """

        self.rect.center = [self.x, self.y]
        return True

    def move_in_pattern(self, path, vel):
        """Moves the enemy in a pattern given a predetermined path (list of coordinate vectors) and speed
        """

        direction = pygame.math.Vector2(path[0]) - (self.x, self.y)

        # if already at dest (first coord in queue), set to enemy pos to dest
        if direction.length() <= vel:
            self.x = path[0][0]
            self.y = path[0][1]
            path.append(path[0])  # and then recycle the pos back into the queue
            path.pop(0)
        else:
            direction.scale_to_length(vel)  # delta dist
            new_pos = pygame.math.Vector2((self.x, self.y)) + direction
            self.x = new_pos.x
            self.y = new_pos.y
            self.update()  # move enemy to new_pos

        cur_pos = (self.x, self.y)  # current position of enemy
        return cur_pos

    def create_bullet(self, image, angle, speed, spin_delta):
        """Creates enemy bullets using EnemyBullets constructor
        """

        return EnemyBullets(image, self.rect.centerx, self.rect.centery, angle, speed, spin_delta)


def draw_health_bar(surf, x, y, health, max_health):
    """Draws the health bar of the Enemy object
    """

    if health > 0:
        health_bar = pygame.Surface([(health / max_health) * 500, y / 2])
        health_bar.fill((255, 255, 0))
        health_bar_rect = health_bar.get_rect()
        health_bar_rect.center = [x, y]
        surf.blit(health_bar, health_bar_rect)
