import pygame
from consts import tile_images, TILE_W, TILE_H


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_W * pos_x, TILE_H * pos_y)
