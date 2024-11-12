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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game.is_playing:
                game.start()  
            elif event.key == pygame.K_SPACE and game.is_playing:
                game.blocks.sprites()[-1].stop()
                game.spawn_block()
                game.score += 1

    if game.is_playing:
        game.update(dt)
    else:
        menu.display()   

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
