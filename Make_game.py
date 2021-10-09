import pygame
import cv2

pygame.init()# 초기화한다.

#화면 크기 설정
screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("My Game")

running = True # 게임이 진행 중

#배경 이미지들 불러오기
background1 = pygame.image.load("C:/Users/tlseh/OneDrive/문서/GitHub/Making game/2DGP Game Source File/Tile Map.png")


# 이벤트 루프 실행
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창이 닫히면
            running = False# 게임 종

    screen.blit(background1,(0, 0))

    pygame.display.update()

#pygame 종료
pygame.quit()