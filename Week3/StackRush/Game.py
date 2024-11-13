import pygame
from Block import Block

class Game:

    def __init__(self):
        self.blocks = pygame.sprite.Group()
        self.orientation = 'left'
        self.is_playing = False
        self.score = 0
        self.screen = pygame.display.get_surface()
        self.run = True
        self.time_since_last_increase = 0

    def spawn_block(self):
        block = Block()

        if len(self.blocks) >= 1 and len(self.blocks) % 20 == 0:
            blocks = pygame.sprite.Group()
            self.blocks.sprites()[-2].rect.y = self.screen.get_height() - block.height
            self.blocks.sprites()[-1].rect.y = self.screen.get_height() - 30 
            blocks.add(self.blocks.sprites()[-2])
            blocks.add(self.blocks.sprites()[-1])
            self.blocks = blocks

        if len(self.blocks) == 0:
            block.rect.x = (self.screen.get_width() // 2) - block.width // 2
            block.rect.y = self.screen.get_height() - block.height
            block.moving = False  

        if len(self.blocks) >= 1:
            block.update_block_velocity(self.blocks.sprites()[-1])
            block.rect.y = self.screen.get_height() - 15 * (len(self.blocks)+1) 
            block.moving = True
            if self.orientation == 'left':                    
                block.dir = -1
                block.rect.x = self.screen.get_width()
                self.orientation = 'right'
            elif self.orientation == 'right':
                block.dir = 1
                block.rect.x = -block.width
                self.orientation = 'left' 
            
        self.blocks.add(block)

    def start(self):
        self.is_playing = True
        self.spawn_block()
        self.spawn_block()

    def game_over(self):
        self.score = 0
        self.is_playing = False
        self.blocks = pygame.sprite.Group()

    def update(self, dt):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        self.screen.blit(score_text, (20, 20))

        if len(self.blocks) > 0:
            moving_block = self.blocks.sprites()[-1]
            self.time_since_last_increase += dt
            if (self.time_since_last_increase >= 3):
                moving_block.velocity += 30
                self.time_since_last_increase = 0
            moving_block.move(dt)
            print(moving_block.velocity)
            if moving_block.rect.x >= self.screen.get_width():
                self.game_over()
            elif moving_block.rect.x < -100:
                self.game_over()

        self.blocks.draw(self.screen)
