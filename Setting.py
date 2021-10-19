import pygame

# 캐릭터의 서있기, 달리기, 이동, 방향
standing_count = 1
running_count = 1
to_x_pos = 0
to_y_pos = 0
dir = 4

#FPS
clock = pygame.time.Clock()

#화면 크기 설정
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# 캐릭터 이동 거리
move_default_x = -0.4
move_default_y = -0.4

#이동 속도 배수
move_speed = 15

# 적 이동 거리
move_enemy_x = -0.3
move_enemy_y = -0.3

#캐릭터 불러오기
character = pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_up.png")
character_size = character.get_rect().size # 이미지 크기를 구해온다.
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = screen_width / 2 # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height # 캐릭터의 세로 위치