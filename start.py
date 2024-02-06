import pygame
from util import terminate
from consts import W, H, FPS, load_image
from main_game import game


def start_screen(sc: pygame.display):
    intro_text = ["OOO, MARIO!", "", "", "", "", "", "", "", "", "",
                  "Вы играете за персонажа Марио!",
                  "Он умеет ходить на одну клетку",
                  "в любом направлении",
                  "Для передвижения используйте WASD"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (W, H))
    sc.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        sc.blit(string_rendered, intro_rect)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return game(sc)
        pygame.display.flip()
        clock.tick(FPS)
