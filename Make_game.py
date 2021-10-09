import pygame

pygame.init()# 초기화한다.

#화면 크기 설정
screen_width = 1280
screen_height = 960

pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("My Game")

running = True

# 이벤트 루프 실행
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




pygame.init()