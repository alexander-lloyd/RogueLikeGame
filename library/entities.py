import pygame


class Entity(pygame.sprite.DirtySprite):
    pass


class Player(Entity):
    def __init__(self):
        super(Player, self).__init__()

    def notify(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pass

    def render(self, surface: pygame.Surface):
        pass

    def update(self, dt: int):
        pass


class Tile(pygame.sprite.DirtySprite):
    def __init__(self, block_path):
        super(Tile, self).__init__()
        self.block_path = block_path