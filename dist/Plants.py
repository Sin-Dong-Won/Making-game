import pygame
import math

import Game_FrameWork
import Game_World
import Load_Asset as load
import Setting as Set
import random
import Map_1 as map
import colilision
import server

screen = Set.screen
screen_width = Set.screen_width
screen_height = Set.screen_height

# 오코이드 프레임 속도
Plants_TIME_PER_RUN = 7
Plants_RUN_PER_TIME = 2.0 / Plants_TIME_PER_RUN
Plants_FRAMES_PER_RUN = 1

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
        self.stand_frame = (self.stand_frame + Plants_FRAMES_PER_RUN * Plants_TIME_PER_RUN * Game_FrameWork.frame_time) % 14

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = self.stand_frame

    def attacking(self):
        self.attack_frame = (self.attack_frame + Plants_FRAMES_PER_RUN * Plants_TIME_PER_RUN * Game_FrameWork.frame_time) % 14
        math.floor(self.attack_frame)

        if math.floor(self.attack_frame) == 5:
            self.attack_count += 1

        if self.attack_count == 4:
            self.fire_peanut()
            self.attack_count = 0

        self.cur = self.attack
        self.cur_sheet = self.attack_sheet
        self.cur_frame = self.attack_frame

    def fire_peanut(self):
        peanut = Peanut((self.x, self.y), self.dir)
        Game_World.add_object(peanut, 1)

    def event(self):
        if self.detect() is False:
            self.standing()
        else:
            self.attacking()

    def draw(self):
        screen.blit(self.cur[self.dir], (self.x, self.y), self.cur_sheet[self.dir][int(self.cur_frame)])
        # pygame.draw.rect(screen, Set.RED, self.get_bounding_box(), 2)

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

        colilision.out_in_map(self)
        self.event()

    def collide(self):
        for i in server.all_Enemy:
            if self is not i:
                colilision.collide(self, i)


class Peanut:
    def __init__(self, plant, dir):
        self.x = plant[0] + 32
        self.y = plant[1] + 32
        self.dir = (dir - 0.5) * 2
        self.target = server.character.x + server.character.width // 2, server.character.y + server.character.height // 2

        self.plant_x = self.x
        self.plant_y = self.y

        self.peanut = load.Plant_Peanut
        self.peanut_sheet = load.Peanut_rect

        self.peanut_frame = 0
        self.peanut_frame_speed = 0
        self.peanut_t = 0

        self.distance = 0

    def get_bounding_box(self):
        return self.x, self.y, self.peanut.get_height(), self.peanut.get_height()

    def draw(self):
        screen.blit(self.peanut, (self.x, self.y), self.peanut_sheet[self.peanut_frame])
        # pygame.draw.rect(screen, Set.RED, self.get_bounding_box(), 2)

    def update(self):
        self.x, self.y = ((1 - self.peanut_t / 100) * self.x) + (self.peanut_t / 100 * self.target[0]), ((1 - self.peanut_t / 100) * self.y) + (self.peanut_t / 100 * self.target[1])
        self.peanut_frame = (self.peanut_frame + 1) % 8

        self.peanut_t += 2

        self.distance = math.sqrt(abs(self.target[0] - self.x) ** 2 + abs(self.target[1] - self.y))

        if colilision.collide(self, server.character) is False:
            server.character.hp -= 1
            Game_World.remove_object(self)

        if self.distance < 3 or self.peanut_t == 100:
            Game_World.remove_object(self)
