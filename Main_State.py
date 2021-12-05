from pygame import *
import pygame
import Game_World as Game_world
import Game_FrameWork as Game_framework
import Setting as Set
import Boss_State
from Character import Character
from Map_1 import Map
from Spider import Spider
from Oconid import Oconid
from Plants import Plants

name = "MainState"
screen = Set.screen
character = None

spiders = []  # (spider1, spider2, spider3, spider4) = (None, None, None, None)
oconids = []  # (oconid1, oconid2, oconid3, oconid4) = (None, None, None, None)
plants = []

test_map = Map()

player_info = (640, 480)
map_bbox = Map.get_bounding_box(test_map)
character_pos = (640, 480)

ENEMY_SPIDER = 5
ENEMY_OCONID = 3
ENEMY_PLANTS = 2


def collide(a, b):
    a_x, a_y, a_w, a_h = a.get_bounding_box()
    b_x, b_y, b_w, b_h = b.get_bounding_box()
    left_a, bottom_a, right_a, top_a = a_x, a_y, a_x + a_w, a_y + a_h
    left_b, bottom_b, right_b, top_b = b_x, b_y, b_x + b_w, b_y + b_h

    if left_a < right_b and abs(left_a - right_b) < a_w // 2 and abs(a_y - b_y) < a_h // 2:
        a.x += abs(left_a - right_b)
        return False

    if right_a > left_b and abs(right_a - left_b) < a_w // 2 and abs(a_y - b_y) < a_h // 2:
        a.x -= abs(right_a - left_b)
        return False

    if bottom_a < top_b and abs(bottom_a - top_b) < a_h // 2 and abs(a_x - b_x) < a_w // 2:
        a.y += abs(bottom_a - top_b)
        return False

    if top_a > bottom_b and abs(top_a - bottom_b) < a_h // 2 and abs(a_x - b_x) < a_w // 2:
        a.y -= abs(top_a - bottom_b)
        return False

    return True


def enter():
    global character
    global spiders
    global oconids

    Game_world.add_object(test_map, 0)  # 게임 월드에 맵 객체 추가
    for spider_list in range(ENEMY_SPIDER):
        spider = Spider()
        spiders.append(spider)
        Game_world.add_object(spider, 1)

    for oconid_list in range(ENEMY_OCONID):
        oconid = Oconid()
        oconids.append(oconid)
        Game_world.add_object(oconid, 1)

    for plant_list in range(ENEMY_PLANTS):
        plant = Plants()
        plants.append(plant)
        Game_world.add_object(plant, 1)

    character = Character()
    Game_world.add_object(character, 1)  # 게임 월드에 캐릭터 개체 추가


def exit():
    global character, test_map, spiders, oconids, plants
    del character
    del test_map
    del spiders
    del oconids
    del plants

    Game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            Game_framework.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Game_framework.quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            Game_framework.change_state(Boss_State)

            break
        else:
            character.handle_event(event)


def update():
    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update()  # 업데이트 한다.

    for oconid in oconids:
        if character is not None:
            collide(character, oconid)


BLACK = (255, 255, 255)


def draw():
    screen.fill(BLACK)
    test_map.draw()
    character.draw()

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    pygame.display.update()
