import pygame
import math

import Game_FrameWork
import Load_Asset as load
import Setting as Set
import random
import Map_1 as map
import colilision
import server


class dummy:
    def __init__(self):
        self.x = 10000
        self.y = 10000
        pass

    # 오코이드의 바운딩 박스

    # 오코이드 스탠딩
    def stand(self):
        pass

    def get_bounding_box(self):
        return [self.x, self.y, 1, 1]

    # 오코이드 워킹
    def walk(self):
        pass

    def move_pos(self):
        pass

    def move(self):
        pass

    def chase(self):
        pass

    def event(self, des):
        pass

    def direction(self):
        pass

    def draw(self):
        pass

    def detect(self):
        pass

    def update(self):
        pass

    def collide(self):
        pass

    def out_map(self):
        pass

    def out_map_des(self):
        pass
