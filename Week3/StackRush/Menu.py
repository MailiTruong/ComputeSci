import pygame

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("monospace", 16)
        self.input =""
        self.screen = pygame.display.get_surface()

    def display(self):
        text_surface = self.font.render("Press enter to start", 1, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)


