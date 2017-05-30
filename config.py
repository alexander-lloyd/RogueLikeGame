import logging

import pygame

class GameConfig:
    LOG_LEVEL = logging.DEBUG
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

    FPS = 60

    COLOUR_BLACK = (0, 0, 0)
    COLOUR_RED = (255, 0, 0)

    # Custom Events
    CHANGE_STATE_EVENT = pygame.USEREVENT + 1
