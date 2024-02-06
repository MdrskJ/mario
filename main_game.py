import pygame
from util import load_level, generate_level, terminate
from consts import FPS


def move_player(direction, player_x, player_y, field_map, level_x, level_y):
    new_x, new_y = player_x, player_y
    print(new_x, new_y)
    field_map[new_y][new_x] = '.'
    if direction == 'left':
        if player_x > 0 and field_map[player_y][player_x - 1] != '#':
            new_x, new_y = new_x - 1, new_y
    if direction == 'right':
        if player_x < level_x - 1 and field_map[player_y][player_x + 1] != '#':
            new_x, new_y = new_x + 1, new_y
    if direction == 'up':
        if player_x > 0 and field_map[player_y - 1][player_x] != '#':
            new_x, new_y = new_x, new_y - 1
    if direction == 'down':
        if player_x < level_y - 1 and field_map[player_y + 1][player_x] != '#':
            new_x, new_y = new_x, new_y + 1
    field_map[new_y][new_x] = '@'
    print(new_x, new_y)
    return new_x, new_y


def game(sc: pygame.display):
    player = None
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    field_map = load_level('level1.txt')
    player, level_x, level_y, player_x, player_y = generate_level(field_map,
                                                                  all_sprites,
                                                                  tiles_group,
                                                                  player_group)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                player_x, player_y = move_player('up',
                                                 player_x, player_y,
                                                 field_map,
                                                 level_x, level_y)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                player_x, player_y = move_player('down',
                                                 player_x, player_y,
                                                 field_map,
                                                 level_x, level_y)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                player_x, player_y = move_player('left',
                                                 player_x, player_y,
                                                 field_map,
                                                 level_x, level_y)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                player_x, player_y = move_player('right',
                                                 player_x, player_y,
                                                 field_map,
                                                 level_x, level_y)
        all_sprites.update(player_x, player_y)
        all_sprites.draw(sc)
        pygame.display.flip()
        clock.tick(FPS)
