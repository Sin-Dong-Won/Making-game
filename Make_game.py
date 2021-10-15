import pygame
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
background1 = pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Map/Tile Map 1.png")

#캐릭터 불러오기
character = pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Character/Character_Standing/character_standing_down.png")
character_size = character.get_rect().size # 이미지 크기를 구해온다.
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = screen_width / 2 # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height # 캐릭터의 세로 위치

# 캐릭터 이동 거리는 음의 12의 배수
move_default_x = -12
move_default_y = -12

# 캐릭터의 스탠딩 모션
character_standing_Left = [pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Character_Standing/character_standing_down.png"),
                           pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Character_Standing/character_standing 2.png"),
                           pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Character_Standing/character_standing 3.png"),
                           pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Character_Standing/character_standing 4.png")]

standing_count = 0

to_x_pos = 0
to_y_pos = 0

# 이벤트 함수 구현
def what_events():
    global running
    global move_default_x
    global move_default_y
    global to_x_pos
    global to_y_pos

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:  # 창이 닫히면
            running = False  # 게임 종료

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # ESC를 누르면
            running = False  # 게임 종료

        elif event.type == pygame.KEYDOWN:  # 키 입력
            if event.key == pygame.K_LEFT:  # 좌
                to_x_pos = move_default_x
            elif event.key == pygame.K_RIGHT:  # 우
                to_x_pos = -move_default_x
            elif event.key == pygame.K_UP:  # 상
                to_y_pos = move_default_y
            elif event.key == pygame.K_DOWN:  # 하
                to_y_pos = -move_default_y

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
    global standing_count

    if to_x_pos == 0 and to_y_pos == 0:
        screen.blit(character_standing_Left[standing_count % 4], (character_x_pos, character_y_pos))
        standing_count += 1


# 이벤트 루프 실행
while running:
    dt = clock.tick(15)

    what_events()

    character_x_pos += to_x_pos
    character_y_pos += to_y_pos

    screen.blit(background1,(0, 0))
    Standing()
    Out_in_Map()

    pygame.display.update()

#pygame 종료
pygame.quit()