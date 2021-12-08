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
import server
import colilision

name = "FisrtState"
screen = Set.screen

test_map = Map()

ENEMY_SPIDER = 0
ENEMY_OCONID = 0
ENEMY_PLANTS = 0


def enter():
    server.map = Map()
    Game_world.add_object(server.map, 0)  # 게임 월드에 맵 객체 추가

    Game_world.add_object(server.character, 1)
    server.character.x, server.character.y = 1080, 480

    server.spiders = [Spider() for i in range(ENEMY_SPIDER)]
    Game_world.add_objects(server.spiders, 1)

    server.oconids = [Oconid() for i in range(ENEMY_OCONID)]
    Game_world.add_objects(server.oconids, 1)

    server.plants = [Plants() for i in range(ENEMY_PLANTS)]
    Game_world.add_objects(server.plants, 1)


def exit():
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
            if colilision.clear_in(server.character, server.map):
                Game_framework.change_state(Boss_State)

            break
        else:
            server.character.handle_event(event)


def update():
    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update()  # 업데이트 한다.


BLACK = (255, 255, 255)


def draw():
    screen.fill(BLACK)
    server.map.draw()
    server.character.draw()

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    pygame.display.update()
