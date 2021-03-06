import pygame

# 바운딩 박스 색깔 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 화면 크기 설정
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# 캐릭터 이동 거리
move_default_x = -2
move_default_y = -2

# 이동 속도 배수
move_speed = 15

# 적 이동 거리
move_enemy_x = -0.3
move_enemy_y = -0.3

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Character/Character_Standing/character_standing_up.png")
character_size = character.get_rect().size  # 이미지 크기를 구해온다.
character_width = character_size[0]  # 가로
character_height = character_size[1]  # 세로
character_x_pos = screen_width / 2  # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height  # 캐릭터의 세로 위치
