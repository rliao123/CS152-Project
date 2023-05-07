import pygame
import math


alt_color = False # used for alternate color switching

class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle, speed, spin_delta):
        """Constructor for EnemyBullets class
        """

        super().__init__()
        self.image = pygame.transform.rotate(image, angle + spin_delta)  # set rotation of the constructed sprite
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.spin_delta = spin_delta  # angle delta

    def update(self):
        """Updates the state of the rect/bullet-sprite to the EnemyBullet object's new position
        """

        # increment rect pos to new pos by the bullet's speed, also factors in angle direction
        self.rect.x -= self.speed * math.cos(math.radians(self.angle + self.spin_delta))
        self.rect.y += self.speed * math.sin(math.radians(self.angle + self.spin_delta))

        # delete bullet when reaches edge of screen window
        if self.rect.top < 0 or self.rect.bottom > 600 or self.rect.right > 600 or self.rect.left < 0:
            self.kill()

    def draw(self, surface):
        """Draws the EnemyBullet image on its rect
        """

        surface.blit(self.image, self.rect)
