import logging
import pygame

from config import GameConfig
from .display import DisplayManager


class Game:
    def __init__(self):
        self.running = True

        self.logger = logging.Logger("Game")
        self.logger.debug("Starting Game")

        Game.init()
        self.display_manager = DisplayManager()

        self.temp_surface = pygame.Surface(GameConfig.SCREEN_DIMENSIONS)

    def run(self):
        self._gameloop()

    @staticmethod
    def init():
        pygame.init()

    @staticmethod
    def quit():
        pygame.quit()

    def _gameloop(self):
        self.display_manager.create_screen()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.render()
            pygame.time.delay(50)

        Game.quit()

    def render(self):
        self.temp_surface.fill(GameConfig.COLOUR_BLACK)

        self.display_manager.main_surface.blit(self.temp_surface, (0, 0))

        pygame.display.flip()
