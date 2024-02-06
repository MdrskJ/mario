import pygame
from consts import player_image, TILE_W, TILE_H


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            TILE_W * pos_x + 15, TILE_H * pos_y + 5)

    def update(self, new_x, new_y):
        self.rect = self.image.get_rect().move(
            TILE_W * new_x + 15, TILE_H * new_y + 5)
