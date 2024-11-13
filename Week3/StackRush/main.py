import pygame
from Game import Game
from Menu import Menu

pygame.init()

pygame.display.set_caption("StackRush")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game = Game()
menu = Menu()
game.run = True
dt = 0

while game.run:

    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False

        if not game.is_playing:
            menu.event_handler(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game.is_playing:
                game.start()  
            elif event.key == pygame.K_SPACE and game.is_playing:
                moving_block = game.blocks.sprites()[-1]
                moving_block.stop()
                if len(game.blocks) > 1:
                    static_block = game.blocks.sprites()[-2]
                    if moving_block.rect.x >= static_block.rect.x + static_block.width or moving_block.rect.x + moving_block.width <= static_block.rect.x:
                        game.game_over()
                    else:
                        overlap_width = moving_block.width - abs(moving_block.rect.x - static_block.rect.x)
                        moving_block.update_block_width(overlap_width)
                        moving_block.update_block_rect(static_block)
                        game.spawn_block()                        
                        game.blocks.sprites()[-1].update_block_width(overlap_width)
                        game.score += 1

    if game.is_playing:
        game.update(dt)
    else:
        menu.update()
        menu.display(screen) 

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
