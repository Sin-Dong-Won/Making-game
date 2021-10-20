import random
import pygame
import math
import Load_Asset as load
import Setting as set
screen = set.screen


class Character:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

        self.stand = load.character_standing
        self.run = load.character_running
        self.attack = load.character_attacking
        self.weapon = load.weapon_attacking
        self.now_do = self.stand

        self.frame = load.frame
        self.attack_frame = load.attack_frame

        self.sheet1 = 0
        self.sheet2 = 0

        self.move_speed = set.move_speed
        self.run_speed = 0
        self.attack_speed = 0

        self.running = True
        self.events = 0
        self.event = 0

        self.to_x_pos = 0
        self.to_y_pos = 0

        self.dir = 0
        self.move_default_x = set.move_default_x
        self.move_default_y = set.move_default_y

    def Events(self):

        self.events = pygame.event.get()

        for self.event in self.events:
            if self.event.type == pygame.QUIT:  # 창이 닫히면
                self.running = False  # 게임 종료

            elif self.event.type == pygame.KEYDOWN and self.event.key == pygame.K_ESCAPE:  # ESC를 누르면
                self.running = False  # 게임 종료

            elif self.event.type == pygame.KEYDOWN:  # 키 입력

                if self.event.key == pygame.K_UP:  # 상
                    self.to_y_pos = self.move_default_y
                    self.dir = 0
                    self.now_do = self.run
                elif self.event.key == pygame.K_DOWN:  # 하
                    self.to_y_pos = -self.move_default_y
                    self.dir = 1
                    self.now_do = self.run
                elif self.event.key == pygame.K_LEFT:  # 좌
                    self.to_x_pos = self.move_default_x
                    self.dir = 2
                    self.now_do = self.run
                elif self.event.key == pygame.K_RIGHT:  # 우
                    self.to_x_pos = -self.move_default_x
                    self.dir = 3
                    self.now_do = self.run
                if self.event.key == pygame.K_SPACE:
                    self.now_do = self.attack

            elif self.event.type == pygame.KEYUP:
                if self.event.key == pygame.K_LEFT or self.event.key == pygame.K_RIGHT:
                    self.to_x_pos = 0
                    self.now_do = self.stand
                elif self.event.key == pygame.K_UP or self.event.key == pygame.K_DOWN:
                    self.to_y_pos = 0
                    self.now_do = self.stand

        self.x += self.to_x_pos * self.move_speed
        self.y += self.to_y_pos * self.move_speed

        self.x, self.y = Out_in_Map(self.x, self.y)

        self.Do()

    def Do(self):
        if self.now_do == self.stand:
            self.Stand()
        elif self.now_do == self.run:
            self.Run()
        elif self.now_do == self.attack:
            self.Attack()

    def Stand(self):
        screen.blit(self.stand[self.dir], (self.x, self.y))

    def Run(self):
        self.sheet1 = load.rects2
        screen.blit(self.run[self.dir], (self.x, self.y), self.sheet1[self.dir][self.frame])

        self.run_speed += 0.1
        self.frame = math.floor(self.run_speed)
        self.frame = (self.frame + 1) % 4

        if self.frame == 0:
            self.run_speed = 0

    def Attack(self):
        self.sheet1 = load.attack_rect2
        self.sheet2 = load.weapon_rect2

        screen.blit(self.weapon[self.dir], (self.x - 16, self.y - 16), self.sheet2[self.dir][self.attack_frame])
        screen.blit(self.attack[self.dir], (self.x, self.y), self.sheet1[self.dir][self.attack_frame])

        self.attack_speed += 0.1
        self.attack_frame = math.floor((self.attack_speed))
        self.attack_frame = (self.attack_frame + 1) % 5

        if self.attack_frame == 0:
            self.now_do = self.stand
            self.attack_speed = 0
            screen.blit(self.stand[self.dir], (self.x, self.y))


# 거미 객체 만들기
class Spider:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0
        self.dir_x = 0
        self.dir_y = 0

        self.stand_frame = 0
        self.stand_frame_speed = 0

        self.walk_frame = 0
        self.walk_frame_speed = 0

        self.standing = load.Spider_standing
        self.walking = load.Spider_walking

        self.address = False
        self.walk_destination = (0, 0)
        self.t = 0
        self.per = 0

    def Update(self, dir):
        global Spider_standing_frame
        if dir == 0:
            self.dir = dir

        elif dir == 1:
            self.dir = dir

        elif dir == 2:
            self.dir = dir

        elif dir == 3:
            self.dir = dir

    # 거미 스탠딩
    def Standing(self):
        screen.blit(self.standing[self.dir_y][self.stand_frame], (self.x, self.y))

        # 거미의 스탠딩 속도
        self.stand_frame_speed += 0.1
        self.stand_frame = math.floor(self.stand_frame_speed)
        self.stand_frame = (self.stand_frame + 1) % 4

        if self.stand_frame == 0:
            self.stand_frame_speed = 0

    # 거미가 향할 목적지
    def Walk_Pos(self, p):
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

    # 거미 워킹
    def Walking(self):

        self.t = self.t + 2
        self.per = self.t / 100

        if self.x != self.walk_destination[0]:
            self.x = (1 - self.per) * self.x + self.per * self.walk_destination[0]

            screen.blit(self.walking[self.dir_x][self.walk_frame], (self.x, self.y))

            self.walk_frame_speed += 0.1
            self.walk_frame = math.floor(self.walk_frame_speed)
            self.walk_frame = (self.walk_frame + 1) % 4

            if self.walk_frame == 0:
                self.walk_frame_speed = 0

            if self.x == self.walk_destination[0]:
                self.t = 0

        elif self.y != self.walk_destination[1]:
            self.y = (1 - self.per) * self.y + self.per * self.walk_destination[1]

            screen.blit(self.walking[self.dir_y][self.walk_frame], (self.x, self.y))

            self.walk_frame_speed += 0.1
            self.walk_frame = math.floor((self.walk_frame_speed))
            self.walk_frame = (self.walk_frame + 1) % 4

            if self.walk_frame == 0:
                self.walk_frame_speed = 0

            if self.y == self.walk_destination[1]:
                self.t = 0

    def Events(self, p):
        if self.address == False:
            self.address = self.Move_Event(True, p)

        else:
            if abs(self.x - p[0]) > 10 or abs(self.y - p[1]) > 10:
                self.Move_Event(True, p)
                self.Walking()

            elif abs(self.x - p[0]) < 5 and abs(self.y - p[1]) < 5:
                self.Standing()

            else:
                self.Walking()


    def Move_Event(self, Move, p):
        if Move == True:
            self.Walk_Pos(p)

            return True
        else:
            return False


# 오코이드 개체 만들기
class Oconid:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0
        self.dir_x = 0
        self.dir_y = 0

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
            if abs(self.x - p[0]) > 10 or abs(self.y - p[1]) > 10:
                self.Move_Event(True, p)
                self.Walk()

            elif abs(self.x - p[0]) < 5 and abs(self.y - p[1]) < 5:
                self.Stand(self.dir)

            else:
                self.Walk()

    def Move_Event(self, Move, p):
        if Move == True:
            self.Move_Pos(p)

            return True
        else:
            return False


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




