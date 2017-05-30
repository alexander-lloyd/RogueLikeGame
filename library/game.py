import logging
import os

import pygame

from config import GameConfig
from library.display import DisplayManager
from library.event import EventManager, EventListener
from library.resources import Resources
from library.states import State

os.environ['SDL_VIDEO_CENTERED'] = "1"


class Game(EventListener):
    def __init__(self):
        self.running = True

        self.logger = logging.Logger("Game")
        self.logger.setLevel(GameConfig.LOG_LEVEL)
        self.logger.debug("Starting Game")

        Game.init()
        self.display_manager = DisplayManager()
        DisplayManager.set_icon(Resources.icon)
        self.clock = pygame.time.Clock()
        self.eventManager = EventManager()
        self.eventManager.add_listener(self)

        self.temp_surface = None

        self.states = {}
        self.current_state = None

        self.show_fps = False
        self.caption = 'RogueLike Game'

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
        # Loading Screen
        self.temp_surface = pygame.display.get_surface()

        Resources.load_resources()

        while self.running:
            dt = self.clock.tick(GameConfig.FPS) / 1000.0
            self.check_events()
            self.update(dt)
            surface = self.render(self.temp_surface)

            self.display_manager.main_surface.blit(surface, (0, 0))
            pygame.display.flip()

        Game.quit()

    def render(self, surface: pygame.Surface):
        if self.show_fps:
            fps = self.clock.get_fps()
            caption = "{} - {:.2f} FPS".format(self.caption, fps)
        else:
            caption = self.caption
        pygame.display.set_caption(caption)
        surface = self.current_state.render(surface)
        return surface

    def update(self, dt: int):
        self.current_state.update(dt)

    def check_events(self):
        for event in pygame.event.get():
            self.eventManager.notify(event)

    def notify(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_F1:
                self.display_manager.toggle_full_screen()
            elif event.key == pygame.K_F5:
                self.show_fps = not self.show_fps
        elif event.type == GameConfig.CHANGE_STATE_EVENT:
            new_state = event.new_state
            self.set_current_state(new_state)

    def add_state(self, state_name: str, state: State):
        state.set_event_manager(self.eventManager)
        self.states.update({state_name: state})
        self.eventManager.add_listener(state)

    def set_current_state(self, state: str):
        self.current_state = self.states.get(state)
