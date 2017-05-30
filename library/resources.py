import os

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
        sprites = [[None] * number_y] * number_x

        for x in range(number_x):
            for y in range(number_y):
                rect = pygame.Rect(x * (tile_width + margin), y * (tile_height + margin), tile_width, tile_height)
                if x == 1 and y == 1:
                    print(rect)
                image = pygame.Surface(rect.size)
                image.blit(self.surface, (0, 0), rect)
                sprites[x][y] = image

        return sprites

    def load_at(self, rect: pygame.Rect):
        image = pygame.Surface(rect.size)
        image.fill((0, 0, 0, 255))
        image.blit(self.surface, (0, 0), rect)
        image.set_colorkey((0, 0, 0), pygame.RLEACCEL)

        return image


class Resources:
    icon = pygame.image.load('assets/icon.png')
    icon2 = pygame.transform.scale2x(icon)

    @staticmethod
    def load_resources():
        Resources.no_texture = pygame.image.load('assets/notexture.png').convert_alpha()

        Resources.__character_sheet = SpriteSheet('assets/character.png')

        Resources.character = Resources.__character_sheet.load_at(pygame.Rect(17, 17, 16, 16))

    @staticmethod
    def load_all_gfx(directory: str, accept=('.png', '.jpg', '.bmp')):
        for picture in os.listdir(directory):
            name, ext = os.path.splitext(picture)
            if ext.lower() in accept:
                img = pygame.image.load(os.path.join(directory, picture))
                if img.get_alpha():
                    img = img.convert_alpha()
                else:
                    img = img.convert()
                Resources.__dict__['img_' + name] = img

    @staticmethod
    def _load_generic_item(directory: str, accept: tuple, prefix='file_'):
        for item in os.listdir(directory):
            name, ext = os.path.splitext(item)
            if ext.lower() in accept:
                Resources.__dict__[prefix + name] = os.path.join(directory, item)

    @staticmethod
    def load_all_music(directory: str, accept=('.mp3', '.wav', '.ogg', '.mdi')):
        Resources._load_generic_item(directory, accept, 'sound')

    @staticmethod
    def load_all_fonts(directory: str, accept=('.ttf',)):
        Resources._load_generic_item(directory, accept, 'font')

    @staticmethod
    def load_all_music(directory: str, accept=('.mp3', '.wav', '.ogg', '.mdi')):
        Resources._load_generic_item(directory, accept, 'sound')

    @staticmethod
    def load_all_sfx(directory: str, accept=('.mp3', '.wav', '.ogg', '.mdi')):
        Resources._load_generic_item(directory, accept, 'sfx')

        for variable, path in [(variable, path) for variable, path in Resources.__dict__.items() if
                               variable.startswith('sfx')]:
            Resources.__dict__[variable] = pygame.mixer.Sound(path)
