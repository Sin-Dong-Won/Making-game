import random
import pygame
import math
import Load_Asset as load
import Setting as set
import Game_World as world
screen = set.screen


class Plants:
    def __init__(self, p, dir):
        self.x = p[0]
        self.y = p[1]

        self.dir = dir

        self.stand = load.Plant
        self.attack = load.Plant_Attack

        self.stand_sheet = load.Plant_rect2
        self.attack_sheet = load.Plant_Attack_rect2

        self.frame = 0
        self.frame_speed = 0

        self.attack_frame = 0
        self.attack_frame_speed = 0

    def Stand(self):
        screen.blit(self.stand[self.dir], (self.x, self.y), self.stand_sheet[self.dir][self.frame])

        self.frame_speed += 0.1
        self.frame = math.floor((self.frame_speed))
        self.frame = (self.frame + 1) % 14

    def Attack(self):
        screen.blit(self.attack[self.dir], (self.x, self.y), self.attack_sheet[self.dir][self.attack_frame])

        self.attack_frame_speed += 0.1
        self.attack_frame = math.floor((self.attack_frame_speed))
        self.attack_frame = (self.attack_frame + 1) % 14

        peanut = Peanut((self.x, self.y))
        world.all_objects(peanut, 1)


    def Detect(self, target):
        if abs(self.x - target[0]) < 96 and abs(self.y - target[1]) < 480:
            self.frame = self.attack_frame
            if self.dir == 0 and self.y < target[1]:
                self.Attack()

            elif self.dir == 1 and self.y < target[1]:
                self.Attack()

        else:
            self.attack_frame = self.frame
            self.Stand()


    def get_Event(self, target):
        self.Detect(target)

class Peanut:
    image = None

    def __init__(self, p):
        self.x = p[0] + 32
        self.y = p[1] + 32

        self.peanut_time_count = 0

        self.peanut = load.Plant_Peanut
        self.peanut_sheet = load.Peanut_rect

        self.peanut_frame = 0
        self.peanut_frame_speed = 0

        self.peanut_count = 0
        self.peanut_create = 0

    def Peanut_Flying(self):
        if self.peanut_count < 40:
            screen.blit(self.peanut, (self.peanut_x, self.peanut_y), self.peanut_sheet[self.peanut_frame])

            self.peanut_y += 12
            self.peanut_count += 1

            self.peanut_frame_speed += 0.1
            self.peanut_frame = math.floor((self.peanut_frame_speed))
            self.peanut_frame = (self.peanut_frame + 1) % 8

        else:
            self.peanut_x = self.x + 32
            self.peanut_y = self.y + 32
            self.peanut_create = 0



screen_width = set.screen_width
screen_height = set.screen_height
character_width = set.character_width
character_height = set.character_height

# 맵 밖에 나갔는지 검사

def Out_in_Map(x_pos, y_pos):

    if (x_pos < 72) or (x_pos > screen_width - 144) or (y_pos < 72) or (y_pos > screen_height - 160):

        if (x_pos < 72):
            x_pos = 0 + 72

        elif (x_pos > screen_width - 144):
            x_pos = screen_width - 144

        if (y_pos < 72):
            y_pos = 0 + 72

        elif (y_pos > screen_height - 160):
            y_pos = screen_height - 160

    return x_pos, y_pos




