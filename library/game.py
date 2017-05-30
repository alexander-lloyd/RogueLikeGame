import logging
import pygame

from config import GameConfig
from .display import DisplayManager
from .event import EventListener, EventManager


class Game(EventListener):
    def notify(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def __init__(self):
        self.running = True

        self.logger = logging.Logger("Game")
        self.logger.debug("Starting Game")

        Game.init()
        self.display_manager = DisplayManager()
        self.clock = pygame.time.Clock()
        self.eventManager = EventManager()
        self.eventManager.add_listener(self)

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
        self.temp_surface = self.temp_surface.convert()

        while self.running:
            self.check_events()

            self.render()
            self.clock.tick(GameConfig.FPS)

        Game.quit()

    def render(self):
        self.temp_surface.fill(GameConfig.COLOUR_RED)

        self.display_manager.main_surface.blit(self.temp_surface, (0, 0))

        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            self.eventManager.notify(event)
