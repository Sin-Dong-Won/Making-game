import pygame
import math
import Load_Asset as load
import Setting as set
import random
import Player_Information as player


screen = set.screen


# 거미 객체 만들기
class Spider:
    def __init__(self):
        self.x = 640
        self.y = 320
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

    # 거미 스탠딩
    def stand(self):
        # 거미의 스탠딩 속도
        self.dir = 1
        self.stand_frame_speed += 0.1
        self.stand_frame = math.floor(self.stand_frame_speed)
        self.stand_frame = (self.stand_frame + 1) % 4

        self.cur = self.standing
        self.cur_frame = self.stand_frame
        self.cur_frame_speed = self.stand_frame_speed

        if self.stand_frame == 0:
            self.stand_frame_speed = 0

    # 거미 워킹
    def walk(self):
        self.walk_frame_speed += 0.1
        self.walk_frame = math.floor(self.walk_frame_speed)
        self.walk_frame = (self.walk_frame + 1) % 4

        self.cur = self.walking
        self.cur_frame = self.walk_frame
        self.cur_frame_speed = self.walk_frame_speed

        if self.walk_frame == 0:
            self.walk_frame_speed = 0

    def move_pos(self):
        self.des = (self.x + random.randint(-100, 100), self.y + random.randint(-100, 100))
        self.prev_des = self.des

        return self.des

    def move(self):
        self.x = ((1 - self.t / 100) * self.x) + (self.t / 100 * self.des[0])
        self.y = ((1 - self.t / 100) * self.y) + (self.t / 100 * self.des[1])

        self.t += 1
        self.walk()

        if self.t == 100:
            self.chase_t = 0
            self.t = 0
            self.des = None
            self.cycle = 0

    def chase(self):
        self.x = ((1 - self.chase_t/ 100) * self.x) + (self.chase_t / 100 * self.des[0])
        self.y = ((1 - self.chase_t / 100) * self.y) + (self.chase_t / 100 * self.des[1])

        self.chase_t += 1
        self.walk()

        if self.chase_t == 100:
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
        screen.blit(self.cur[self.dir][self.cur_frame], (self.x, self.y))

    def detect(self):
        if math.sqrt((self.x - self.player_pos[0]) ** 2 + (self.x - self.player_pos[1]) ** 2) < 200:
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
        print(position)

        self.event(position)


