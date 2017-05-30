from abc import abstractmethod

import pygame

from config import GameConfig
from library.entities import Entity
from library.event import EventListener, EventManager
from library.resources import Resources


class BaseState(EventListener):
    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass

    @abstractmethod
    def update(self, dt: float):
        pass


class State(BaseState):
    def __init__(self):
        self.event_manager = None

        self.entities = []

    def set_event_manager(self, event_manager: EventManager):
        self.event_manager = event_manager

    def add_entities(self, entity: Entity):
        self.entities.append(entity)


class SplashScreen(State):
    logo = Resources.icon2

    def __init__(self):
        super(SplashScreen, self).__init__()
        self.screen_width = (None, None)

        self.time_to_wait = 5.0

    def render(self, surface: pygame.Surface):
        surface.fill(GameConfig.COLOUR_RED)
        rect = surface.get_rect()
        image = SplashScreen.logo
        image_rect = image.get_rect()
        mid_x = rect.w / 2 - (image_rect.w / 2)
        mid_y = rect.h / 2 - (image_rect.h / 2)
        surface.blit(SplashScreen.logo, (mid_x, mid_y))
        return surface

    def update(self, dt: float):
        self.time_to_wait -= dt
        if self.time_to_wait < 0:
            change_state_event = pygame.event.Event(GameConfig.CHANGE_STATE_EVENT, {'new_state': 'game'})
            pygame.event.post(change_state_event)

    def notify(self, event: pygame.event.Event):
        pass


class GameScreen(State):

    def update(self, dt: float):
        pass

    def notify(self, event: pygame.event.Event):
        pass

    def render(self, surface: pygame.Surface):
        surface.fill(GameConfig.COLOUR_BLACK)
        return surface
