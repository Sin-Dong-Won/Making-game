import pygame
import math

import Game_FrameWork
import Load_Asset as load
import Setting as set
import random
import Map_1 as map

screen = set.screen
screen_width = set.screen_width
screen_height = set.screen_height

# 거미 이동 속도
PIXEL_PER_METER = (1.0 / 0.3)  # 1 pixel 30 cm
Spider_SPEED_KMPH = 2.0  # Km / Hour
Spider_SPEED_MPM = (Spider_SPEED_KMPH * 100.0 / 60.0)
Spider_SPEED_MPS = (Spider_SPEED_MPM / 6.0)
Spider_SPEED_PPS = (Spider_SPEED_MPS * PIXEL_PER_METER)


# 거미 프레임 속도
Spider_TIME_PER_RUN = 0.5
Spider_RUN_PER_TIME = 2.0 / Spider_TIME_PER_RUN
Spider_FRAMES_PER_RUN = 1

# 거미 이동 범위
range_default = 200
range_x_min = -range_default
range_x_max = range_default
range_y_min = -range_default
range_y_max = range_default

# Spider Size
Sp_width = load.spider_size.width
Sp_height = load.spider_size.height

Sp_bb_start_x = Sp_width
Sp_bb_start_y = Sp_height

left_map, bottom_map, right_map, top_map = [map.bg_bb_start_x, map.bg_bb_start_y, map.bg_width, map.bg_height]


# 거미 객체 만들기
class Spider:
    def __init__(self):
        self.x = random.randint(100, 1000)
        self.y = random.randint(100, 1000)
        self.dir = 0

        self.prev_des = None
        self.des = None
        self.player_pos = 0

        self.t = 0
        self.chase_t = 0
        self.cycle = 0

        self.stand_frame = 0
        self.stand_frame_speed = 0

        self.walk_frame = 0
        self.walk_frame_speed = 0

        self.standing = load.Spider_standing
        self.walking = load.Spider_walking

        self.cur = self.standing
        self.cur_frame = 0
        self.cur_frame_speed = 0

    # 거미의 바운딩 박스
    def get_bounding_box(self):
        return [self.x, self.y, Sp_width, Sp_height]

    # 거미 스탠딩
    def stand(self):
        # 거미의 스탠딩 속도
        self.dir = 1

        self.stand_frame = (self.stand_frame + Spider_FRAMES_PER_RUN * Spider_RUN_PER_TIME * Game_FrameWork.frame_time) % 4

        self.cur = self.standing
        self.cur_frame = self.stand_frame
        self.cur_frame_speed = self.stand_frame_speed

        if self.stand_frame == 0:
            self.stand_frame_speed = 0

    # 거미 워킹
    def walk(self):
        self.walk_frame_speed += 0.2
        self.walk_frame = math.floor(self.walk_frame_speed)
        self.walk_frame = (self.walk_frame + 1) % 4

        self.cur = self.walking
        self.cur_frame = self.walk_frame
        self.cur_frame_speed = self.walk_frame_speed

        if self.walk_frame == 0:
            self.walk_frame_speed = 0

    def move_pos(self):
        self.des = (self.x + random.randint(range_x_min, range_x_max), self.y + random.randint(range_y_min, range_y_max))
        self.prev_des = self.des

        if self.out_map_des() is False:
            self.move_pos()

        else:
            return self.des

    def move(self):
        self.x = ((1 - self.t / 100) * self.x) + (self.t / 100 * self.des[0])
        self.y = ((1 - self.t / 100) * self.y) + (self.t / 100 * self.des[1])

        self.t += 2
        self.walk()

        if self.t == 100:
            self.chase_t = 0
            self.t = 0
            self.des = None
            self.cycle = 0

    def chase(self):
        self.x = ((1 - self.chase_t / 100) * self.x) + (self.chase_t / 100 * self.des[0])
        self.y = ((1 - self.chase_t / 100) * self.y) + (self.chase_t / 100 * self.des[1])

        self.chase_t += 2
        self.walk()

        if self.chase_t == 100 or (abs(self.x - self.des[0]) < 10 and abs(self.y - self.des[1]) < 10):
            self.chase_t = 0
            self.t = 0
            self.des = None
            self.cycle = 0

    def event(self, des):
        if self.des is None:
            self.des = self.move_pos()

        else:
            self.direction()
            if self.cycle > 100:
                self.detect()
                if self.des == self.prev_des:
                    self.move()
                else:
                    self.chase()

            else:
                self.stand()
                self.cycle += 1

        map_out = self.out_map()

        if map_out is False:
            self.des = None
            self.cycle = 0

        self.draw()

    def direction(self):
        if self.des is not None:
            if self.x < self.des[0] and abs(self.x - self.des[0]) > abs(self.y - self.des[1]):
                self.dir = 3

            elif self.x < self.des[0] and abs(self.x - self.des[0]) < abs(self.y - self.des[1]):
                if self.y - self.des[1] < 0:
                    self.dir = 1
                elif self.y - self.des[1] > 0:
                    self.dir = 0

            elif self.x >= self.des[0] and abs(self.x - self.des[0]) > abs(self.y - self.des[1]):
                self.dir = 2

            elif self.x >= self.des[0] and abs(self.x - self.des[0]) < abs(self.y - self.des[1]):
                if self.y - self.des[1] < 0:
                    self.dir = 1
                elif self.y - self.des[1] > 0:
                    self.dir = 0

            else:
                self.dir = 1

    def draw(self):
        screen.blit(self.cur[self.dir][int(self.cur_frame)], (self.x, self.y))
        # pygame.draw.rect(screen, set.RED, self.get_bounding_box(), 2)

    def detect(self):
        if math.sqrt((self.x - self.player_pos[0]) ** 2 + (self.x - self.player_pos[1]) ** 2) < 100:
            self.des = self.player_pos

        else:
            self.des = self.prev_des

        return self.des

    def update(self):
        file = open('player_pos.txt', 'r')
        position = file.readline()
        position = position.split(' ')
        tuple(position)
        position = (int(position[0]), int(position[1]))

        self.player_pos = position

        self.event(position)

    def out_map(self):
        global range_x_min, range_x_max, range_y_min, range_y_max

        if self.x < left_map:
            self.x = map.bg_bb_start_x
            return False

        elif self.x > right_map:
            self.x = map.bg_width
            return False
        elif self.y > top_map:
            self.y = map.bg_height
            return False

        elif self.y < bottom_map:
            self.y = map.bg_bb_start_y
            return False

        return True

    def out_map_des(self):
        global range_x_min, range_x_max, range_y_min, range_y_max

        if self.des[0] < map.bg_bb_start_x:
            range_x_min = range_x_min + range_default
            range_x_max = range_x_max + range_default
            return False
        if self.des[0] > map.bg_width:
            range_x_min = range_x_min - range_default
            range_x_max = range_x_max - range_default
            return False
        if self.des[1] < map.bg_bb_start_y:
            range_y_min = range_y_min + range_default
            range_y_max = range_y_max + range_default
            return False
        if self.des[1] > map.bg_height:
            range_y_min = range_y_min - range_default
            range_y_max = range_y_max - range_default
            return False

        range_x_min = -range_default
        range_x_max = range_default
        range_y_min = -range_default
        range_y_max = range_default
        return True
