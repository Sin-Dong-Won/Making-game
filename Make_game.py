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

spider = obj.Spider()
spider.Load((0, 0))

character = obj.Character()
character.Load((640, 480))

map1 = load.background1
screen = set.screen
clock = set.clock
i = 0
# 이벤트 루프 실행
while running:
    dt = clock.tick(60)

    screen.blit(map1,(0, 0))

    character.Events()
    running = character.running

    pygame.display.update()

pygame.quit()








