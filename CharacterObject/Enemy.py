import pygame


class Enemy(pygame.sprite.Sprite):
    debug = True

    def __init__(self, w, h, x, y, max_health):
        super().__init__()
        self.image = pygame.Surface([w, h])  # replace with image later
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.x = x
        self.y = y
        self.max_health = max_health
        self.health = max_health
        self.iterator = 0

    def update(self):
        self.rect.center = [self.x, self.y]
        if debug:
            print(self.rect.center)
        return True

    def move(self, x, y, vel):
        ax, bx = self.x, x
        ay, by = self.y, y
        dx, dy = (bx - ax), (by - ay)
        step_x, step_y = (dx / 60.), (dy / 60.)  # float

        self.x = self.x + vel * step_x
        self.y = self.y + vel * step_y
        self.update()

        if self.x != x or self.y != y:
            return False  # not finished moving
        else:
            return True  # finished moving

    def pattern1(self):
        match self.iterator:
            case 0:
                m1 = self.move(150, 150, 4)
                if m1:
                    self.iterator += 1
            case 1:
                m2 = self.move(450, 150, 4)
                if m2:
                    self.iterator += 1
