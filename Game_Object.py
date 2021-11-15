import random
import pygame
import math
import Load_Asset as load
import Setting as set
import Game_World as world
screen = set.screen


# 오코이드 개체 만들기
class Oconid:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0
        self.dir_x = 0
        self.dir_y = 0
        self.distance = 0

        self.frame = 0
        self.frame_speed = 0

        self.move = load.Oconid
        self.sheet = load.oconid_rect2

        self.address = False
        self.walk_destination = (0, 0)
        self.t = 0
        self.per = 0

    def Stand(self, dir):
        self.dir = dir
        screen.blit(self.move[self.dir], (self.x, self.y), self.sheet[self.dir][self.frame])

        self.frame_speed += 0.125
        self.frame = math.floor((self.frame_speed))
        self.frame = (self.frame + 1) % 8

    def Walk(self):

        self.t = self.t + 2
        self.per = self.t / 100

        if self.y != self.walk_destination[1]:
            self.y = (1 - self.per) * self.y + self.per * self.walk_destination[1]

            screen.blit(self.move[self.dir_y], (self.x, self.y), self.sheet[self.dir][self.frame])

            self.frame_speed += 0.125
            self.frame = math.floor(self.frame_speed)
            self.frame = (self.frame + 1) % 8

            if self.frame == 0:
                self.frame_speed = 0

            if self.y == self.walk_destination[1]:
                self.t = 0

        elif self.x != self.walk_destination[0]:
            self.x = (1 - self.per) * self.x + self.per * self.walk_destination[0]

            screen.blit(self.move[self.dir_x], (self.x, self.y), self.sheet[self.dir][self.frame])

            self.frame_speed += 0.125
            self.frame = math.floor((self.frame_speed))
            self.frame = (self.frame + 1) % 8

            if self.frame == 0:
                self.frame_speed = 0

            if self.x == self.walk_destination[0]:
                self.t = 0

    def Move_Pos(self, p):
        self.walk_destination = ((p[0], p[1]))
        self.walk_destination = Out_in_Map(self.walk_destination[0], self.walk_destination[1])

        if self.x < self.walk_destination[0]:
            self.dir_x = 3

        elif self.x > self.walk_destination[0]:
            self.dir_x = 2

        if self.y < self.walk_destination[1]:
            self.dir_y = 1

        elif self.x > self.walk_destination[1]:
            self.dir_y = 0

    def Events(self, move, p):
        if self.address == False:
            self.address = self.Move_Event(True, p)

        else:
            self.distance = math.sqrt((self.x - p[0]) ** 2 + (self.y - p[1]) ** 2)

            if self.distance < 200:
                self.Move_Event(True, p)
                self.Walk()

            else:
                self.Stand(self.dir)

    def Move_Event(self, Move, p):
        if Move == True:
            self.Move_Pos(p)

            return True
        else:
            return False

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




