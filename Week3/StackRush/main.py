import pygame
from Game import Game
from Menu import Menu

pygame.init()

#set game and menu instances and clock
pygame.display.set_caption("StackRush")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

game = Game()
menu = Menu()
game.run = True
dt = 0

#game loop
while game.run:

    screen.fill([255, 255, 255])

    #handle quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.run = False

    #check all events everytime
        if not game.is_playing:
            menu.check_event(event)
        game.check_event(event)

    #store the name and update the game
    if game.is_playing:
        game.player.name = menu.player_name
        game.update(dt)
    else:#if it's not playing the menu displays
        menu.update()
        menu.display(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
