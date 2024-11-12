import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 15
        self.color = (0, 0, 0)
        self.velocity = 100
        self.image = pygame.Surface((self.width, 15))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.moving = False
        self.dir = -1

    def move(self, dt):
        if self.moving:
            self.rect.x += self.velocity * dt * self.dir

    def stop(self):
        self.moving = False


