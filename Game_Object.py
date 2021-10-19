import pygame
import math
import Load_Asset as load
import Setting as set

screen = set.screen

class Character:
    def Load(self, p):
        self.x = p[0]
        self.y = p[0]

        self.stand = load.character_standing
        self.run = load.character_running
        self.attack = load.character_attacking
        self.weapon = load.weapon_attacking
        self.now_do = 0

        self.frame = load.frame
        self.attack_frame = load.attack_frame

        self.sheet1 = 0
        self.sheet2 = 0

        self.move_speed = set.move_speed
        self.run_speed = 0
        self.attack_speed = 0

        self.running = True

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
        screen.blit(self.run[self.dir],(self.x, self.y), self.sheet1[self.dir][self.frame])

        self.run_speed += 0.25
        self.frame = math.floor((self.run_speed))
        self.frame = (self.frame + 1) % 4

    def Attack(self):
        self.sheet1 = load.attack_rect2
        self.sheet2 = load.weapon_rect2

        screen.blit(self.attack[self.dir], (self.x, self.y), self.sheet1[self.dir][self.attack_frame])
        screen.blit(self.weapon[self.dir], (self.x - 16, self.y - 16), self.sheet2[self.dir][self.attack_frame])

        self.attack_speed += 0.25
        self.attack_frame = math.floor((self.attack_speed))
        self.attack_frame = (self.attack_frame + 1) % 5

        if self.attack_frame == 0:
            self.now_do = self.stand
            self.attack_speed = 0


# 거미 객체 만들기
class Spider:
    def Load(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0

        self.frame = 0
        self.frame_speed = 0
        self.standing = load.Spider_standing

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

        # 거미의 속도
        self.frame_speed += 0.2
        self.frame = math.floor((self.frame_speed))
        self.frame = (self.frame + 1) % 4

    # 그리기
    def Draw(self):
        set.screen.blit(load.Spider_standing[self.dir][self.frame], (self.x, self.y))


screen_width = set.screen_width
screen_height = set.screen_height
character_width = set.character_width
character_height = set.character_height

def Out_in_Map(x_pos, y_pos):

    if (x_pos < 0):
        print(5)
        x_pos = 0
    elif (x_pos > screen_width - 64):
        print(5)
        y_pos = screen_width - character_width
    if (y_pos < 0):
        print(5)
        y_pos = 0
    elif (y_pos > screen_height - 64):
        print(5)
        y_pos = screen_height - character_height





