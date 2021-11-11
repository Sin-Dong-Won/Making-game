import pygame
import math
import Load_Asset as load
import Setting as set
import random
screen = set.screen


# 거미 객체 만들기
class Spider:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0

        self.prev_des = 0
        self.des = 0

        self.t = 0
        self.chase_t = 0

        self.stand_frame = 0
        self.stand_frame_speed = 0

        self.walk_frame = 0
        self.walk_frame_speed = 0

        self.standing = load.Spider_standing
        self.walking = load.Spider_walking

        self.cur = 0
        self.cur_frame = 0
        self.cur_frame_speed = 0

    # 거미 스탠딩
    def stand(self):

        # 거미의 스탠딩 속도
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
        self.des = (self.x + random.randint(10 , 100), self.y + random.randint(10 , 100))
        self.prev_des = self.des
        self.t = 0

    def move(self):
        self.x = ((1 - self.t / 100) * self.x) + ((self.t / 100) * self.des[0])
        self.y = ((1 - self.t / 100) * self.x) + ((self.t / 100) * self.des[1])

        self.t += 1

        if self.t == 100:
            self.t = 0
            self.des = 0

    def chase(self, des):
        self.des = des

        self.x = ((1 - self.t / 100) * self.x) + ((self.t / 100) * self.des[0])
        self.y = ((1 - self.t / 100) * self.x) + ((self.t / 100) * self.des[1])

        self.chase_t += 1

        if self.chase_t == 100:
            self.chase_t = 0
            self.des = 0

    def event(self, des):
        if self.des == self.prev_des:
            self.move()

        else:
            if self.des == 0:
                self.move_pos()
                self.move()

            else:
                self.chase(des)

        self.draw()

    def direction(self, p):
        if self.x < p[0] and abs(self.x - p[0]) > abs(self.y - p[1]):
            self.dir = 3

        elif self.x < p[0] and abs(self.x - p[0]) < abs(self.y - p[1]):
            if self.y - p[1] < 0:
                self.dir = 0
            elif self.y - p[1] > 0:
                self.dir = 1

        elif self.x >= p[0] and abs(self.x - p[0]) > abs(self.y - p[1]):
            self.dir = 2

        elif self.x >= p[0] and abs(self.x - p[0]) < abs(self.y - p[1]):
            if self.y - p[1] < 0:
                self.dir = 0
            elif self.y - p[1] > 0:
                self.dir = 1

        else:
            self.dir = 1

        return self.dir

    def draw(self):
        self.dir = self.direction(self.des)
        screen.blit(self.cur[self.dir][self.cur_frame],(self.x, self.y))



