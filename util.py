import sys
import pygame

from tiles import Tile
from player import Player


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level, all_sprites, tiles_group, player_group):
    new_player, x, y = None, None, None
    W, H = len(level[1]), len(level)
    for y in range(H):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, tiles_group, all_sprites)
            elif level[y][x] == '#':
                Tile('wall', x, y, tiles_group, all_sprites)
            elif level[y][x] == '@':
                Tile('empty', x, y, tiles_group, all_sprites)
                player_x, player_y = x, y
    new_player = Player(player_x, player_y, player_group, all_sprites)
    return new_player, W, H, player_x, player_y


def terminate():
    pygame.quit()
    sys.exit()
