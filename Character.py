import random
import pygame
import math
import Load_Asset as load
import Setting as set
import Game_World as world
screen = set.screen

# Boy Event
RIGHT_KEY_DOWN, LEFT_KEY_DOWN, RIGHT_KEY_UP, LEFT_KEY_UP, UP_KEY_UP, UP_KEY_DOWN, DOWN_KEY_DOWN, DOWN_KEY_UP, SLEEP_TIMER, KEY_ITEM, ATTACK_KEY_DO, ATTACK_KEY_STOP = range(12)

key_event_table = {
    (pygame.KEYDOWN, pygame.K_UP): UP_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_DOWN): DOWN_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_LEFT): LEFT_KEY_DOWN,
    (pygame.KEYDOWN, pygame.K_RIGHT): RIGHT_KEY_DOWN,

    (pygame.KEYUP, pygame.K_UP): UP_KEY_UP,
    (pygame.KEYUP, pygame.K_DOWN): DOWN_KEY_UP,
    (pygame.KEYUP, pygame.K_LEFT): LEFT_KEY_UP,
    (pygame.KEYUP, pygame.K_RIGHT): RIGHT_KEY_UP,

    (pygame.KEYUP, pygame.K_i): KEY_ITEM,
    (pygame.KEYDOWN, pygame.K_i): KEY_ITEM,

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
            self.to_y_pos = set.move_default_y
            self.to_x_pos = 0
            self.dir = 0

        elif event == DOWN_KEY_DOWN:
            self.to_y_pos = -set.move_default_y
            self.to_x_pos = 0
            self.dir = 1

        elif event == LEFT_KEY_DOWN:
            self.to_x_pos = set.move_default_x
            self.to_y_pos = 0
            self.dir = 2

        elif event == RIGHT_KEY_DOWN:
            self.to_x_pos = -set.move_default_x
            self.to_y_pos = 0
            self.dir = 3

        self.sheet1 = load.rects2

    def exit(self, event):
        pass

    def update(self):
        self.x += self.to_x_pos
        self.y += self.to_y_pos

        self.run_frame_speed += 0.1
        self.frame = math.floor(self.run_frame_speed)
        self.frame = (self.frame + 1) % 4

        if self.frame == 0:
            self.run_speed = 0

    def draw(self):
        screen.blit(self.run[self.dir], (self.x, self.y), self.sheet1[self.dir][self.frame])


class AttackState:
    def enter(self, event):
        self.attack_frame = 0
        self.attack_speed = 0
        self.sheet1 = load.attack_rect2
        self.sheet2 = load.weapon_rect2

    def exit(self, event):
        pass

    def update(self):
        self.attack_speed += 0.25
        self.attack_frame = math.floor((self.attack_speed))
        self.attack_frame = (self.attack_frame + 1) % 5



        if self.attack_frame == 0:
            self.attack_frame = 0
            self.attack_speed = 0

        else:
            self.draw()

    def draw(self):
        screen.blit(self.attack[self.dir], (self.x, self.y), self.sheet1[self.dir][self.attack_frame])


next_state_table = {
    StandState: {UP_KEY_DOWN: MoveState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: MoveState, DOWN_KEY_UP: StandState,
                 LEFT_KEY_DOWN: MoveState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: MoveState, RIGHT_KEY_UP: StandState,
                 ATTACK_KEY_DO: AttackState, ATTACK_KEY_STOP: StandState},

    MoveState: {UP_KEY_DOWN: StandState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: StandState, DOWN_KEY_UP: StandState,
                LEFT_KEY_DOWN: StandState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: StandState, RIGHT_KEY_UP: StandState,
                ATTACK_KEY_DO: AttackState, ATTACK_KEY_STOP: StandState},

    AttackState: {UP_KEY_DOWN: StandState, UP_KEY_UP: StandState, DOWN_KEY_DOWN: StandState, DOWN_KEY_UP: StandState,
                  LEFT_KEY_DOWN: StandState, LEFT_KEY_UP: StandState, RIGHT_KEY_DOWN: StandState, RIGHT_KEY_UP: StandState,
                  ATTACK_KEY_DO: StandState, ATTACK_KEY_STOP: StandState}
}


class Character:
    def __init__(self):
        self.x = 640
        self.y = 480

        self.stand = load.character_standing
        self.run = load.character_running
        self.attack = load.character_attacking
        self.weapon = load.weapon_attacking
        self.inventory = load.inventory

        self.frame = load.frame
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

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.update(self)

        self.file = open("player_pos.txt", 'w')
        data = '%d %d' % (self.x, self.y)

        self.file.write(data)
        self.file.close()

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print((event.type, event.key))
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)




