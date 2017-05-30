from abc import ABC

import pygame


class EventListener(ABC):
    def notify(self, event: pygame.event.Event):
        raise NotImplementedError()


class EventManager:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener: EventListener):
        """
        :param listener: object that wants to listener to events
        :return: None
        
        When adding a listener, this method takes care of creating a creating a reference in the dict above and adding 
        the listener object to it.
        """

        assert isinstance(listener, EventListener)
        self.listeners.append(listener)

    def delete_listener(self, listener: EventListener):
        self.listeners.remove(listener)

    def notify(self, event: pygame.event.Event):
        for listener in self.listeners:
            listener.notify(event)
