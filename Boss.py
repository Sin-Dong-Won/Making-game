import pygame
import math

import Game_World
import Load_Asset as load
import Setting as set
import random
import Map_1 as map

screen = set.screen
screen_width = set.screen_width
screen_height = set.screen_height

# 식물 Size
pl_width = load.plant_size.width // 8
pl_height = load.plant_size.height

pl_bb_start_x = pl_width
pl_bb_start_y = pl_height

pl_attack_width = load.plant_attack_size.width // 8
pl_attack_height = load.plant_attack_size.height

pl_bb_attack_start_x = pl_width
pl_bb_attack_start_y = pl_height

left_map, bottom_map, right_map, top_map = [map.bg_bb_start_x, map.bg_bb_start_y, map.bg_width, map.bg_height]
bg_bb_start_x = 84
bg_width = load.background1_size.width - bg_bb_start_x * 2


# 보스 객체 만들기
class SlimeBoss:
    def __init__(self):
        self.x = 400
        self.y = 120
        self.dir = 0
        self.now_x = self.x
        self.now_y = self.y

        self.enemy = None
        self.attack_count = 0

        self.stand_frame = 0
        self.stand_frame_speed = 0

        self.attack_frame = 0
        self.attack_frame_speed = 0

        self.stand_sheet = load.BOSS_Stand_rect2
        self.attack_sheet = load.BOSS_Attack_rect2

        self.stand = load.BOSS_Stand
        self.attack = load.BOSS_Attack

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = 0
        self.cur_frame_speed = 0

    # 보스의 바운딩 박스
    def get_bounding_box(self):
        return [self.x, self.y, pl_width, pl_height]

    # 보스 평상시
    def standing(self):
        # 보스의 평상 속도
        self.now_y = self.y
        self.stand_frame_speed += 0.2
        self.stand_frame = math.floor(self.stand_frame_speed)
        self.stand_frame = (self.stand_frame + 1) % 4

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = self.stand_frame
        self.cur_frame_speed = self.stand_frame_speed
        self.attack_frame_speed = 0

        if self.stand_frame == 0:
            self.stand_frame_speed = 0

    def attacking(self):
        self.now_y = self.y - 80
        self.attack_frame_speed += 0.25
        self.attack_frame = math.floor(self.attack_frame_speed)
        self.attack_frame = (self.attack_frame + 1) % 8

        self.attack_count += 1

        self.cur = self.attack
        self.cur_sheet = self.attack_sheet
        self.cur_frame = self.attack_frame
        self.cur_frame_speed = self.attack_frame_speed
        self.stand_frame_speed = 0

        if self.attack_frame == 0:
            self.attack_frame_speed = 0

    def event(self):
        isdetect = self.detect()

        if isdetect is True:
            self.attacking()
        else:
            self.standing()

    def draw(self):
        print(self.detect())
        screen.blit(self.cur[self.dir], (self.x, self.now_y), self.cur_sheet[self.dir][self.cur_frame])
        # pygame.draw.rect(screen, set.RED, self.get_bounding_box(), 2)

    def detect(self):
        if self.x < self.enemy[0]:
            self.dir = 1

        elif self.x >= self.enemy[0]:
            self.dir = 0

        print(self.y)

        print(abs(self.x - self.enemy[0]))
        print(abs(self.y - self.enemy[1]))

        if abs(self.x - self.enemy[0]) < 160 and abs(self.y - self.enemy[1]) < 400:
            return True

        else:
            return False

    def update(self):
        file = open('player_pos.txt', 'r')
        position = file.readline()
        position = position.split(' ')
        tuple(position)
        position = (int(position[0]), int(position[1]))
        self.enemy = (position[0] - 240, position[1])

        self.event()

