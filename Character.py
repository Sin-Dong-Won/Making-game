import pygame

import Load_Asset as load
import Setting as set
import Game_FrameWork
import Game_World
import server
import colilision

screen = set.screen
screen_width = set.screen_width
screen_height = set.screen_height

# Character Default Health
Default_Health = 10
Health_Position_Default = 32

# Character Under Attack
Character_Under_Attack = 0

# Character Coin
Default_Coin = 1000
Coin_Position_Default = 32
Coin_Position_x = screen_width * 0.75

# Character Run Speed
PIXEL_PER_METER = (1.0 / 0.3)  # 1 pixel 30 cm
Character_SPEED_KMPH = 6.0  # Km / Hour
Character_SPEED_MPM = (Character_SPEED_KMPH * 100.0 / 60.0)
Character_SPEED_MPS = (Character_SPEED_MPM / 6.0)
Character_SPEED_PPS = (Character_SPEED_MPS * PIXEL_PER_METER)

# Character Run Frame Speed
TIME_PER_RUN = 0.5
RUN_PER_TIME = 2.0 / TIME_PER_RUN
FRAMES_PER_RUN = 1

# Character Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 6.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1

# Character Size
ch_width = load.character_size.width
ch_height = load.character_size.height
ch_bb_start_x = ch_width // 2
ch_bb_start_y = ch_width * 0.75

# Character Event
RIGHT_KEY_DOWN, LEFT_KEY_DOWN, RIGHT_KEY_UP, LEFT_KEY_UP, UP_KEY_UP, UP_KEY_DOWN, DOWN_KEY_DOWN, DOWN_KEY_UP, SLEEP_TIMER, KEY_ITEM_DOWN, KEY_ITEM_UP, ATTACK_KEY_DO, ATTACK_KEY_STOP = range(13)

key_event_table = {
    (pygame.KEYDOWN, pygame.K_UP): UP_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_DOWN): DOWN_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_LEFT): LEFT_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_RIGHT): RIGHT_KEY_DOWN,

    (pygame.KEYUP, pygame.K_UP): UP_KEY_UP,
    (pygame.KEYUP, pygame.K_DOWN): DOWN_KEY_UP,
    (pygame.KEYUP, pygame.K_LEFT): LEFT_KEY_UP,
    (pygame.KEYUP, pygame.K_RIGHT): RIGHT_KEY_UP,

    (pygame.KEYUP, pygame.K_i): KEY_ITEM_UP,
    (pygame.KEYDOWN, pygame.K_i): KEY_ITEM_DOWN,

    (pygame.KEYUP, pygame.K_SPACE): ATTACK_KEY_STOP,
    (pygame.KEYDOWN, pygame.K_SPACE): ATTACK_KEY_DO
}


class StandState:
    def enter(self, event):
        if event == UP_KEY_DOWN:
            self.to_y_pos = 0
            self.to_x_pos = 0
            self.dir = 0

        elif event == DOWN_KEY_DOWN:
            self.to_y_pos = 0
            self.to_x_pos = 0
            self.dir = 1

        elif event == LEFT_KEY_DOWN:
            self.to_y_pos = 0
            self.to_x_pos = 0
            self.dir = 2

        elif event == RIGHT_KEY_DOWN:
            self.to_y_pos = 0
            self.to_x_pos = 0
            self.dir = 3

    def update(self):
        pass

    def exit(self, event):
        pass

    def draw(self):
        screen.blit(self.stand[self.dir], (self.x, self.y))


class MoveState:
    def enter(self, event):
        if event == UP_KEY_DOWN:
            self.to_y_pos = -Character_SPEED_PPS
            self.to_x_pos = 0
            self.dir = 0

        elif event == DOWN_KEY_DOWN:
            self.to_y_pos = Character_SPEED_PPS
            self.to_x_pos = 0
            self.dir = 1

        elif event == LEFT_KEY_DOWN:
            self.to_x_pos = -Character_SPEED_PPS
            self.to_y_pos = 0
            self.dir = 2

        elif event == RIGHT_KEY_DOWN:
            self.to_x_pos = Character_SPEED_PPS
            self.to_y_pos = 0
            self.dir = 3

        self.sheet1 = load.rects2

    def exit(self, event):
        pass

    def update(self):
        self.x += self.to_x_pos
        self.y += self.to_y_pos

        self.frame = (self.frame + RUN_PER_TIME * FRAMES_PER_RUN * Game_FrameWork.frame_time) % 4

        if self.frame == 0:
            self.run_speed = 0

    def draw(self):
        screen.blit(self.run[self.dir], (self.x, self.y), self.sheet1[self.dir][int(self.frame)])


class AttackState:
    def enter(self, event):
        self.attack_frame = 0
        self.attack_speed = 0
        self.sheet1 = load.attack_rect2
        self.sheet2 = load.weapon_rect2

    def exit(self, event):
        pass

    def update(self):
        self.attack_frame = (self.attack_frame + TIME_PER_ACTION * ACTION_PER_TIME * Game_FrameWork.frame_time) % 5

        for i in server.all_objects:
            if colilision.kill(self, i):
                server.all_objects.remove(i)
                Game_World.remove_object(i)

        if self.attack_frame == 0:
            self.attack_frame = 0
            self.attack_speed = 0

        else:
            self.draw()

    def draw(self):
        screen.blit(self.attack[self.dir], (self.x, self.y), self.sheet1[self.dir][int(self.attack_frame)])


class ItemState:
    def enter(self, event):
        self.image = load.inventory

    def exit(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        screen.blit(self.image, (screen_width // 4, screen_height // 4))


next_state_table = {
    StandState: {UP_KEY_DOWN: MoveState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: MoveState, DOWN_KEY_UP: StandState,
                 LEFT_KEY_DOWN: MoveState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: MoveState, RIGHT_KEY_UP: StandState,
                 ATTACK_KEY_DO: AttackState, ATTACK_KEY_STOP: StandState, KEY_ITEM_DOWN: ItemState, KEY_ITEM_UP: StandState},

    MoveState: {UP_KEY_DOWN: StandState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: StandState, DOWN_KEY_UP: StandState,
                LEFT_KEY_DOWN: StandState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: StandState, RIGHT_KEY_UP: StandState,
                ATTACK_KEY_DO: AttackState, ATTACK_KEY_STOP: StandState, KEY_ITEM_DOWN: ItemState, KEY_ITEM_UP: StandState},

    AttackState: {UP_KEY_DOWN: StandState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: StandState, DOWN_KEY_UP: StandState,
                  LEFT_KEY_DOWN: StandState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: StandState, RIGHT_KEY_UP: StandState,
                  ATTACK_KEY_DO: StandState, ATTACK_KEY_STOP: StandState, KEY_ITEM_DOWN: ItemState, KEY_ITEM_UP: StandState},

    ItemState: {UP_KEY_DOWN: ItemState, UP_KEY_UP: ItemState, DOWN_KEY_DOWN: ItemState, DOWN_KEY_UP: ItemState,
                LEFT_KEY_DOWN: ItemState, LEFT_KEY_UP: ItemState, RIGHT_KEY_DOWN: ItemState, RIGHT_KEY_UP: ItemState,
                ATTACK_KEY_DO: ItemState, ATTACK_KEY_STOP: ItemState, KEY_ITEM_DOWN: StandState, KEY_ITEM_UP: ItemState}
}


class Character:
    def __init__(self):
        self.x = 640
        self.y = 800
        self.hp = Default_Health
        self.coin = Default_Coin

        self.stand = load.character_standing
        self.run = load.character_running
        self.attack = load.character_attacking
        self.weapon = load.weapon_attacking
        self.inventory = load.inventory
        self.health = load.character_health
        self.money = load.Character_Coin
        self.number = load.Numbers

        self.frame = 0
        self.attack_frame = load.attack_frame

        self.sheet1 = 0
        self.sheet2 = 0

        self.move_speed = set.move_speed
        self.run_frame_speed = 0
        self.attack_speed = 0

        self.inventory_open = False

        self.to_x_pos = 0
        self.to_y_pos = 0

        self.dir = 0
        self.move_default_x = set.move_default_x
        self.move_default_y = set.move_default_y

        self.event_que = []
        self.cur_state = StandState
        self.cur_state.enter(self, None)

        self.file = 0
        self.width = ch_width * 0.5
        self.height = ch_height * 0.5

        self.center_x = 0
        self.center_y = 0

        self.start_x = 0
        self.start_y = 0

    # 캐릭터의 바운딩 박스
    def get_box(self):
        if self.cur_state == AttackState:
            return self.get_attacking_box()
        else:
            return self.get_bounding_box()

    def get_bounding_box(self):
        self.center_x = self.x + ch_width // 2
        self.center_y = self.y + ch_height // 2

        self.start_x = (self.x + self.center_x) // 2
        self.start_y = (self.y + self.center_y) // 2

        return [self.start_x, self.start_y, self.width, self.height]

    def get_attacking_box(self):
        if self.dir == 0:
            return [self.start_x, self.start_y - self.height // 2, self.width * 1.5, self.height * 1.5]
        elif self.dir == 1:
            return [self.start_x - self.width // 2, self.start_y, self.width * 1.5, self.height * 1.5]
        elif self.dir == 2:
            return [self.start_x - self.width // 2, self.start_y - self.height // 2, self.width * 1.5, self.height * 1.5]
        elif self.dir == 3:
            return [self.start_x, self.start_y, self.width * 1.5, self.height * 1.5]

        return

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        global Character_Under_Attack

        self.cur_state.update(self)
        self.out_in_map()

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        self.file = open("player_pos.txt", 'w')
        data = '%d %d' % (self.x, self.y)

        self.file.write(data)
        self.file.close()

        for i in server.all_objects:
            if colilision.collide(self, i) is False:
                Character_Under_Attack += 1
                self.under_attack()

    def under_attack(self):
        global Character_Under_Attack

        if Character_Under_Attack > 50:
            self.hp -= 1
            Character_Under_Attack = 0

    def draw(self):
        self.cur_state.draw(self)
        pygame.draw.rect(screen, set.RED, self.get_box(), 2)
        screen.blit(self.money, (Coin_Position_x, Coin_Position_Default // 4))

        self.draw_coin()

        for i in range(self.hp):
            screen.blit(self.health, (i * Health_Position_Default, 0))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if (event.type, event.key) in key_event_table.keys():
                key_event = key_event_table[(event.type, event.key)]
                self.add_event(key_event)

            else:
                pass
        else:
            pass

    def draw_coin(self):
        now_coin = self.coin
        digit = 1

        while now_coin != 0:
            screen.blit(self.number[now_coin % 10], (screen_width - (digit * Coin_Position_Default), 0))
            now_coin = now_coin // 10
            digit += 1

    def out_in_map(self):

        if (self.x < 72) or (self.x > screen_width - 144) or (self.y < 72) or (self.y > screen_height - 160):
            if self.x < 72:
                self.x = 0 + 72

            elif self.x > screen_width - 144:
                self.x = screen_width - 144

            if self.y < 72:
                self.y = 0 + 72

            elif self.y > screen_height - 160:
                self.y = screen_height - 160
