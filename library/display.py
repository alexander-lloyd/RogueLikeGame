import pygame

from config import GameConfig


class DisplayManager:
    def __init__(self):
        self.SCREEN_DIMENSIONS = GameConfig.SCREEN_DIMENSIONS
        self.fullscreen = False

        self.main_surface = None

        if not pygame.display.get_init():
            pygame.display.init()

    def toggle_full_screen(self):
        if pygame.display.get_driver() == 'x11':
            pygame.display.toggle_fullscreen()
            return

        self.fullscreen = not self.fullscreen

        self._set_mode()

    def _set_mode(self):
        if self.fullscreen:
            self.flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        else:
            self.flags = pygame.DOUBLEBUF
        self.main_surface = pygame.display.set_mode(self.SCREEN_DIMENSIONS, self.flags)

    def create_screen(self):
        self._set_mode()

    @staticmethod
    def set_icon(icon: pygame.Surface):
        pygame.display.set_icon(icon)
