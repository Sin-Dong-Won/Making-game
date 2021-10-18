import pygame
import time
import math

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

# 적 이동 거리
move_enemy_x = -0.3
move_enemy_y = -0.3

# 캐릭터의 스탠딩 상 하 좌 우 상좌 상우 하좌 하우
character_standing = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_up.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_down.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_left.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_right.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_upleft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_upright.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_downleft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_downright.png")
    ]

# 캐릭터의 달리기
character_running = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Up_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Down_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Left_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Right_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_UpLeft_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_UpRight_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_DownLeft_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_DownRight_Run.png")
    ]

rects1 = []
rects2 = []

for i in range(len(character_running)):
    list = []
    rects1.append(character_running[i].get_rect())

    for j in range(4):
        list.append(pygame.Rect(64 * (j + 1), 0, rects1[i].width // 4, rects1[i].height))

    rects2.append(list)

# 프레임 설정
frame = 0

# 적 설정
Spider_standing_up = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp4.png")
    ]

Spider_standing_front = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleFront1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleFront2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleFront3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleFront4.png")
    ]

Spider_standing_left = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleLeft1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleLeft2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleLeft3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleLeft4.png")
    ]

Spider_standing_right = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleRight1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleRight2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleRight3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleRight4.png")
    ]

Spider_standing = \
    [
        Spider_standing_up,
        Spider_standing_front,
        Spider_standing_left,
        Spider_standing_right
    ]

Spider_standing_frame = 0

class Spider:
    def Load(self, p):
        self.x = p[0]
        self.y = p[1]
        self.dir = 0

        self.frame = 0
        self.frame_speed = 0
        self.standing = Spider_standing

    def Update(self, dir):
        global Spider_standing_frame
        if dir == 0:
            self.dir = dir

        elif dir == 1:
            self.dir = dir

        elif dir == 2:
            self.dir = dir

        elif dir == 3:
            self.dir = dir

        self.frame_speed += 0.2
        self.frame = math.floor((self.frame_speed))
        self.frame = (self.frame + 1) % 4

    def Draw(self):
        global Spider_standing
        screen.blit(Spider_standing[self.dir][self.frame], (self.x, self.y))


# def Enemy_Spider(p, dir):
#     enemy = Spider((p[0], p[1]), dir)
#     enemy.Load((p[0], p[1]))
#     enemy.Drawing(dir)

standing_count = 1
running_count = 1
to_x_pos = 0
to_y_pos = 0
dir = 4

# 이벤트 함수 구현
def what_events():
    global running
    global character_x_pos
    global character_y_pos
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


    character_x_pos += to_x_pos * move_speed
    character_y_pos += to_y_pos * move_speed

#맵 밖에 나갔는지 검사
def Out_in_Map(x_pos, y_pos):

    if x_pos < 0 :
        x_pos = 0
    elif x_pos > screen_width - 64:
        character_x_pos = screen_width - character_width
    if y_pos < 0:
        y_pos = 0
    elif y_pos > screen_height - 64:
       y_pos = screen_height - character_height

    return True

def Standing():
    global character_standing

    screen.blit(character_standing[dir], (character_x_pos, character_y_pos))
def Running():
    global running_count
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

spider = Spider()
spider2 = Spider()
spider.Load((0, 0))
spider2.Load((640, 480))
# 이벤트 루프 실행
while running:
    dt = clock.tick(60)

    what_events()

    screen.blit(background1,(0, 0))
    spider.Update(1)
    spider.Draw()
    spider2.Update(3)
    spider2.Draw()
    Move()
    Out_in_Map(character_x_pos, character_y_pos)
    pygame.display.update()



#pygame 종료
pygame.quit()