import logging

import pygame


class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename
        self.surface = pygame.image.load(self.filename).convert_alpha()

    def load_all(self, size: (int, int), margin: int):
        sheet_rect = self.surface.get_rect()
        width, height = sheet_rect.w, sheet_rect.h
        tile_width, tile_height = size

        # Number of sprites in the x direction
        number_x = width // (tile_width + margin)
        # Number of sprites in the y direction
        number_y = height // (tile_height + margin)

        # Create the empty list
        sprites = [[None] * (number_y)] * number_x

        for x in range(number_x):
            for y in range(number_y):
                rect = pygame.Rect(x * (tile_width + margin), y * (tile_height + margin), tile_width, tile_height)
                if x==1 and y == 1:
                    print(rect)
                image = pygame.Surface(rect.size)
                image.blit(self.surface, (0, 0), rect)
                sprites[x][y] = image

        return sprites


    def load_at(self, rect: pygame.Rect):
        image = pygame.Surface(rect.size)
        image.fill((0,0,0,255))
        image.blit(self.surface, (0,0), rect)
        image.set_colorkey((0,0,0), pygame.RLEACCEL)

        return image

class Resources:
    icon = pygame.image.load('assets/icon.png')

    no_texture = None
    __character_sheet = None
    character = None

    @staticmethod
    def load_resources():
        Resources.no_texture = pygame.image.load('assets/notexture.png').convert_alpha()

        Resources.__character_sheet = SpriteSheet('assets/character.png')

        Resources.character = Resources.__character_sheet.load_at(pygame.Rect(17,17,16,16))
