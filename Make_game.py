import random
import pygame
import time
import math
import Function as func
import Game_Object as obj
import Load_Asset as load
import Setting as set

# 초기화한다.
pygame.init()

running = True

character = obj.Character((640, 320))
spider = obj.Spider((640, 480))
oconid = obj.Oconid((320, 240))
spider.Update(1)

oconid.Move_Pos((character.x, character.y))
spider.Walk_Pos((character.x, character.y))

map1 = load.background1
screen = set.screen
clock = set.clock

t = 0

# 이벤트 루프 실행
while running:
    dt = clock.tick(60)
    t = t + 1
    character.Events()

    screen.blit(map1,(0, 0))
    spider.Events((character.x, character.y))
    oconid.Events(True, (character.x, character.y))

    character.Events()

    running = character.running
    pygame.display.update()

pygame.quit()








