import pygame
from pico2d import *
import cv2
import time

# 초기화한다.
pygame.init()

#화면 크기 설정
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()

running = True # 게임이 진행 중

#배경 이미지들 불러오기
background1 = pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Map/Tile Map 1.png")

#캐릭터 불러오기
character = pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_up.png")
character_size = character.get_rect().size # 이미지 크기를 구해온다.
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = screen_width / 2 # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height # 캐릭터의 세로 위치

# 캐릭터 이동 거리
move_default_x = -0.4
move_default_y = -0.4

#이동 속도 배수
move_speed = 15

# 캐릭터의 스탠딩 상 하 좌 우 상좌 상우 하좌 하우
character_standing = \
    [
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_up.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_down.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_left.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_right.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_upleft.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_upright.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_downleft.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_downright.png")
    ]

# 캐릭터의 달리기
character_running = \
    [
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_Up_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_Down_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_Left_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_Right_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_UpLeft_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_UpRight_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_DownLeft_Run.png"),
        pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Run/Character_DownRight_Run.png")
    ]

rects1 = []
rects2 = []

for i in range(len(character_running)):
    list = []
    rects1.append(character_running[i].get_rect())

    for j in range(4):
        list.append(pygame.Rect(48 * (j + 1), 0, rects1[i].width // 4, rects1[i].height))

    rects2.append(list)

# 프레임 설정
frame = 0



standing_count = 1
running_count = 1
to_x_pos = 0
to_y_pos = 0
dir = 4

# 이벤트 함수 구현
def what_events():
    global running
    global move_default_x
    global move_default_y
    global to_x_pos
    global to_y_pos
    global dir

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:  # 창이 닫히면
            running = False  # 게임 종료

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESC를 누르면
            running = False  # 게임 종료

        elif event.type == pygame.KEYDOWN:  # 키 입력
            if event.key == pygame.K_UP:  # 상
                to_y_pos = move_default_y
                dir = 0
            elif event.key == pygame.K_DOWN:  # 하
                to_y_pos = -move_default_y
                dir = 1
            elif event.key == pygame.K_LEFT:  # 좌
                to_x_pos = move_default_x
                dir = 2
            elif event.key == pygame.K_RIGHT:  # 우
                to_x_pos = -move_default_x
                dir = 3

            elif event.key == pygame.K_UP and event.key == pygame.K_LEFT:
                to_y_pos = move_default_y
                to_x_pos = move_default_x
                dir = 4
            elif event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
                to_y_pos = move_default_y
                to_x_pos = move_default_x
                dir = 5
            elif event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
                to_y_pos = move_default_y
                to_x_pos = move_default_x
                dir = 6
            elif event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
                to_y_pos = move_default_y
                to_x_pos = move_default_x
                dir = 7

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x_pos = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y_pos = 0


#맵 밖에 나갔는지 검사
def Out_in_Map():
    global character_x_pos
    global character_y_pos

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - 48:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - 48:
        character_y_pos = screen_height - character_height

    return True

def Standing():
    global character_standing

    screen.blit(character_standing[dir], (character_x_pos, character_y_pos))
def Running():
    global running_count
    global rects1
    global rects2
    global frame

    screen.blit(character_running[dir], (character_x_pos, character_y_pos), rects2[dir][frame])

    frame = (frame + 1) % 4

def Move():
    global to_x_pos
    global to_y_pos

    if to_x_pos == 0 and to_y_pos == 0:
        Standing()

    elif to_x_pos != 0 or to_y_pos != 0:
        Running()

# 이벤트 루프 실행
while running:
    dt = clock.tick(60)

    what_events()

    character_x_pos += to_x_pos * move_speed
    character_y_pos += to_y_pos * move_speed

    screen.blit(background1,(0, 0))

    Move()
    Out_in_Map()
    pygame.display.update()

    # 차후 과제: 적 애니메이션 구현 및 충돌판정 구현

#pygame 종료
pygame.quit()