import pygame
from consts import SIZE
from start import start_screen

pygame.init()
sc = pygame.display.set_mode(SIZE)
start_screen(sc)

pygame.quit()
