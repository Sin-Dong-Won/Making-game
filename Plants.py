import pygame
import math

import Game_World
import Load_Asset as load
import Setting as set
import random
import Map_1 as map
import server

screen = set.screen
screen_width = set.screen_width
screen_height = set.screen_height

# 식물 Size
pl_width = load.plant_size.width // 14
pl_height = load.plant_size.height

pl_bb_start_x = pl_width
pl_bb_start_y = pl_height

pl_attack_width = load.plant_attack_size.width // 14
pl_attack_height = load.plant_attack_size.height

pl_bb_attack_start_x = pl_width
pl_bb_attack_start_y = pl_height

left_map, bottom_map, right_map, top_map = [map.bg_bb_start_x, map.bg_bb_start_y, map.bg_width, map.bg_height]
bg_bb_start_x = 84
bg_width = load.background1_size.width - bg_bb_start_x * 2

# 식물 객체 만들기
class Plants:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = random.randint(1, 1)

        if self.dir == 1:
            self.x = random.randint(pl_bb_start_x, bg_width // 2) + self.dir * (bg_width // 2)
            self.y = map.bg_bb_start_y - 40

        elif self.dir == 0:
            self.x = random.randint(pl_bb_start_x, map.bg_width) + self.dir * (bg_width // 2)
            self.y = map.bg_height + 32

        self.isdetect = False
        self.enemy = None
        self.attack_count = 0

        self.stand_frame = 0
        self.stand_frame_speed = 0

        self.attack_frame = 0
        self.attack_frame_speed = 0

        self.stand_sheet = load.Plant_rect2
        self.attack_sheet = load.Plant_Attack_rect2

        self.stand = load.Plant
        self.attack = load.Plant_Attack

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = 0
        self.cur_frame_speed = 0

    # 식물의 바운딩 박스
    def get_bounding_box(self):
        return [self.x + pl_width / 4, self.y + pl_height / 4, pl_width / 2, pl_height / 2]

    # 식물 평상시
    def standing(self):
        # 식물의 평상 속도
        self.stand_frame_speed += 0.2
        self.stand_frame = math.floor(self.stand_frame_speed)
        self.stand_frame = (self.stand_frame + 1) % 14

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = self.stand_frame
        self.cur_frame_speed = self.stand_frame_speed

        if self.stand_frame == 0:
            self.stand_frame_speed = 0

    def attacking(self):
        self.attack_frame_speed += 0.25
        self.attack_frame = math.floor(self.attack_frame_speed)
        self.attack_frame = (self.attack_frame + 1) % 14

        self.attack_count += 1

        if self.attack_count == 24:
            # print("shoot")
            self.attack_count = 0
            self.fire_peanut()

        self.cur = self.attack
        self.cur_sheet = self.attack_sheet
        self.cur_frame = self.attack_frame
        self.cur_frame_speed = self.attack_frame_speed

        if self.attack_frame == 0:
            self.attack_frame_speed = 0

    def fire_peanut(self):
        peanut = Peanut((self.x, self.y), self.dir)
        Game_World.add_object(peanut, 1)

    def event(self):
        if self.detect() is False:
            self.standing()
        else:
            self.attacking()

    def draw(self):
        screen.blit(self.cur[self.dir], (self.x, self.y), self.cur_sheet[self.dir][self.cur_frame])
        pygame.draw.rect(screen, set.RED, self.get_bounding_box(), 2)

    def detect(self):
        if abs(self.x - server.character.x) < 90 and abs(self.y - server.character.y) < 360:
            return True

        else:
            return False

    def update(self):
        file = open('player_pos.txt', 'r')
        position = file.readline()
        position = position.split(' ')
        tuple(position)
        position = (int(position[0]), int(position[1]))

        self.event()


class Peanut:
    def __init__(self, plant, dir):
        self.x = plant[0] + 32
        self.y = plant[1] + 32
        self.dir = (dir - 0.5) * 2

        self.plant_x = self.x
        self.plant_y = self.y

        self.peanut = load.Plant_Peanut
        self.peanut_sheet = load.Peanut_rect

        self.peanut_frame = 0
        self.peanut_frame_speed = 0

        self.velocity = 16

    def draw(self):
        screen.blit(self.peanut, (self.x, self.y), self.peanut_sheet[self.peanut_frame])

    def update(self):
        self.y += self.velocity * self.dir
        self.peanut_frame = (self.peanut_frame + 1) % 8

        if abs(self.plant_y - self.y) > 360:
            Game_World.remove_object(self)
