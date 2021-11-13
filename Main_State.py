from pygame import *
import pygame
import Game_World as Game_world
import Game_FrameWork as Game_framework
import Setting as Set
import Player_Information as player

from Character import Character
from Map_1 import Map
from Spider import Spider

name = "MainState"
screen = Set.screen
character = None
spider = None
test_map = Map()

player_info = player.pos

character_pos = (640, 480)

def enter():
    global character
    global spider
    character = Character()
    spider = Spider()

    Game_world.add_object(test_map, 0)  # 게임 월드에 맵 객체 추가
    Game_world.add_object(character, 1)  # 게임 월드에 캐릭터 개체 추가
    Game_world.add_object(spider, 1)


def exit():
    global character, test_map, spider
    del character
    del test_map
    del spider


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
        else:
            character.handle_event(event)


def update():
    global player_info

    character.update()

    player_info = (character.x, character.y)

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update()  # 업데이트 한다.


BLACK = (0, 0, 0)


def draw():
    screen.fill(BLACK)
    test_map.draw()
    character.draw()

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    pygame.display.update()
