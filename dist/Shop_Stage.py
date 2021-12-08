import pygame
import Boss_State
import Game_World as Game_world
import Game_FrameWork as Game_framework
import Setting as Set
import server
import Shop_Map
import Load_Asset as load
import colilision
import Title_State


name = "Shop_Stage"
screen = Set.screen
character = None
shop_map = Shop_Map.Map()
map_bbox = shop_map.get_bounding_box()


def enter():
    server.map = shop_map
    Game_world.add_object(server.map, 1)
    Game_world.add_object(server.character, 1)

    server.character.x, server.character.y = 128, 480

def exit():
    global character, shop_map
    del character
    del shop_map


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
            if colilision.get_out(server.character, server.map):
                server.map = Boss_State.test_map
                Game_world.remove_object(shop_map)
                Game_framework.change_state(Title_State)
            else:
                pass

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            if colilision.clear_in(server.character, server.map):
                if len(server.character.item) > 0:
                    load.Sell_Sound.play()
                    server.character.item.pop()
                    server.character.coin += 500

            break
        else:
            server.character.handle_event(event)


def update():
    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.update()  # 업데이트 한다.


BLACK = (255, 255, 255)


def draw():
    screen.fill(BLACK)

    for game_object in Game_world.all_objects():  # 게임 월드 내의 모든 오브젝트를 하나씩 꺼내서
        game_object.draw()  # 그린다.

    pygame.display.update()
