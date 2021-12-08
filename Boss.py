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

# Boss Hp
Boss_Hp_Default = 32

# Boss Size
pl_width = load.Boss_size.width // 8
pl_height = load.Boss_size.height

pl_bb_start_x = pl_width
pl_bb_start_y = pl_height

pl_attack_width = load.Boss_attack_size.width // 8
pl_attack_height = load.Boss_attack_size.height

pl_bb_attack_start_x = pl_width
pl_bb_attack_start_y = pl_height

# 오코이드 프레임 속도
Boss_TIME_PER_RUN = 8
Boss_RUN_PER_TIME = 2.0 / Boss_TIME_PER_RUN
Boss_FRAMES_PER_RUN = 1


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
        self.hp = 10
        self.health = load.Boss_Hp

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
    def get_box(self):
        if self.cur == self.stand:
            return self.get_bounding_box()

        elif self.cur == self.attack:
            return self.get_attacking_box()

    def get_bounding_box(self):
        return [self.x + pl_width / 2, self.y + pl_height / 4, pl_width, pl_height / 2]

    def get_attacking_box(self):
        return [self.x + pl_width / 2, self.y, pl_width, pl_height]

    # 보스 평상시
    def standing(self):
        # 보스의 평상 속도
        self.now_y = self.y

        self.stand_frame = (self.stand_frame + Boss_TIME_PER_RUN * Boss_FRAMES_PER_RUN * Game_FrameWork.frame_time) % 4

        self.cur = self.stand
        self.cur_sheet = self.stand_sheet
        self.cur_frame = self.stand_frame

    def attacking(self):
        self.now_y = self.y - 80

        self.attack_frame = (self.attack_frame + Boss_TIME_PER_RUN * Boss_FRAMES_PER_RUN * Game_FrameWork.frame_time) % 8

        self.attack_count += 1

        if colilision.kill(self, server.character):
            server.character.hp -= 0.2

        if self.attack_count > 150:
            self.attack_count = 0

        self.cur = self.attack
        self.cur_sheet = self.attack_sheet
        self.cur_frame = self.attack_frame

    def event(self):
        if self.detect() is True and self.attack_count > 100:
            self.attacking()
        else:
            self.attack_count += 1
            self.standing()

    def draw(self):
        screen.blit(self.cur[self.dir], (self.x, self.now_y), self.cur_sheet[self.dir][int(self.cur_frame)])
        for i in range(math.ceil(self.hp)):
            screen.blit(self.health, (screen_width * 0.375 + i * Boss_Hp_Default, screen_height - Boss_Hp_Default))
        # pygame.draw.rect(screen, Set.RED, self.get_box(), 2)

    def detect(self):
        if self.x < self.enemy[0]:
            self.dir = 1

        elif self.x >= self.enemy[0]:
            self.dir = 0

        if abs(self.x - self.enemy[0]) < 160 and abs(self.y - self.enemy[1]) < 400:
            return True

        else:
            return False

    def update(self):
        self.enemy = (server.character.x - 240, server.character.y)
        self.event()

        if self.hp <= 0:
            server.boss = None
            server.Music = load.Game_Clear_Sound
            Game_World.remove_object(self)
