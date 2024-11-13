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
    
    def update_block_width(self, overlap_width):
        print(overlap_width) 
        self.width = overlap_width
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
         
    def update_block_rect(self, static_block):
        if self.rect.x - static_block.rect.x < 0:
            self.rect.x = static_block.rect.x
    
    def update_block_velocity(self, last_block):
        self.velocity = last_block.velocity
