import pygame
import Setting as set
import Load_Asset as load
import colilision
import server
import Game_World

screen = set.screen


class Crystals:
    def __init__(self, pos):
        self.x = pos.x
        self.y = pos.y
        self.image = load.Character_Crystal

    def get_bounding_box(self):
        return [self.x, self.y, self.image.get_width(), self.image.get_height()]

    def update(self):
        if colilision.get(server.character, self):
            server.character.item.append(self)
            Game_World.remove_object(self)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, set.RED, self.get_bounding_box(), 2)
