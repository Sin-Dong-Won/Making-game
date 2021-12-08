import pygame
import Setting as Set
import Load_Asset as load
import colilision
import server
import Game_World

screen = Set.screen


class Crystals:
    def __init__(self, pos):
        self.x = pos.x
        self.y = pos.y
        self.image = load.Character_Crystal
        self.get_sound = load.Get_Sound

    def get_bounding_box(self):
        return [self.x, self.y, self.image.get_width(), self.image.get_height()]

    def update(self):
        colilision.out_in_map(self)
        if colilision.get(server.character, self):
            self.get_sound.play()
            server.character.item.append(self)
            Game_World.remove_object(self)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, Set.RED, self.get_bounding_box(), 2)
