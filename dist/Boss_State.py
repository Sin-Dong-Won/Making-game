import pygame
import Load_Asset as load
import Game_World as Game_world
import Game_FrameWork as Game_framework
import Setting as Set
import server
from Character import Character
from Map_2 import Map
from Boss import SlimeBoss

name = "BossState"
screen = Set.screen
character = None
boss = SlimeBoss()
test_map = Map()

map_bbox = Map.get_bounding_box(test_map)


def enter():
    global character

    server.character.x, server.character.y = 640, 800
    character = server.character
    Game_world.add_object(character, 1)
    Game_world.add_object(test_map, 0)
    Game_world.add_object(boss, 1)
    server.boss = boss


def exit():
    global character, test_map, boss
    del character
    del test_map
    del boss


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


BLACK = (255, 255, 255)


def draw():
    screen.fill(BLACK)
    test_map.draw()
    character.draw()

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    if server.boss is None:
        server.Music = load.Game_Clear_Sound
        screen.blit(load.Game_Clear, (419, 399))
        # server.Music.play(-1)

    pygame.display.update()
