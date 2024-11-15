import pygame
import serial
from Game import Game
from Menu import Menu

pygame.init()

#set game and menu instances and clock
pygame.display.set_caption("StackRush")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#set serial connexion
ser = serial.Serial('/dev/tty.usbserial-1340', 9600)

game = Game()
menu = Menu()
game.run = True
dt = 0
button_pressed = False

#game loop
while game.run:

    screen.fill([255, 255, 255])

    if ser and ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()  
        if data == "BUTTON_PRESSED":
            event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_SPACE)
            pygame.event.post(event)

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

ser.close()
pygame.quit()
