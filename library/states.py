from abc import ABC, abstractmethod

import pygame

from config import GameConfig
from library.event import EventListener, EventManager


class BaseState(EventListener):
    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass

    @abstractmethod
    def update(self, dt: int):
        pass


class State(BaseState):
    def __init__(self):
        self.event_manager = None

        self.entities = []

    def set_event_manager(self, event_manager: EventManager):
        self.event_manager = event_manager


class SplashScreen(State):
    def render(self, surface: pygame.Surface):
        surface.fill(GameConfig.COLOUR_RED)
        return surface

    def update(self, dt: int):
        pass

    def notify(self, event: pygame.event.Event):
        pass
