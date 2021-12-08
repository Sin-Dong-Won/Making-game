import pygame
import Dummy
import Load_Asset as load
import Shop_Stage
import Character
import Game_World
import Game_World as Game_world
import Game_FrameWork as Game_framework
import Setting as Set
import Boss_State
from Map_1 import Map
from Spider import Spider
from Oconid import Oconid
from Plants import Plants
import server
import colilision

name = "MainState"
screen = Set.screen

test_map = Map()
map_bbox = Map.get_bounding_box(test_map)

ENEMY_SPIDER = 2
ENEMY_OCONID = 2
ENEMY_PLANTS = 1


def enter():
    server.map = test_map
    Game_world.add_object(server.map, 0)  # 게임 월드에 맵 객체 추가

    server.character = Character.Character()
    Game_world.add_object(server.character, 1)

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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            if colilision.get_out(server.character, server.map) and len(server.all_Enemy) == 0:
                Game_framework.change_state(Shop_Stage)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            if colilision.clear_in(server.character, server.map):
                Game_World.remove_object(test_map)
                Game_framework.change_state(Boss_State)

            break
        else:
            server.character.handle_event(event)


def update():
    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update()  # 업데이트 한다.




BLACK = (255, 255, 255)

sound_play = 0

def draw():
    global sound_play
    screen.fill(BLACK)
    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    if len(server.all_Enemy) == 0:
        screen.blit(load.Stage_Clear, (528, 368))
        if sound_play == 0:
            load.Stage_Clear_Sound.play()
            sound_play += 1

    pygame.display.update()
