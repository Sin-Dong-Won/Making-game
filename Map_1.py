import pygame
import Setting as set

screen = set.screen


class Map:
    def __init__(self):
        self.image = pygame.image.load("2DGP Game Source File/Map/Tile Map Test.png")

    def update(self):
        pass

    def draw(self):
        screen.blit(self.image, (0, 0))

