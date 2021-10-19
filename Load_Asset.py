import pygame

background1 = pygame.image.load("C:/Users/tlseh/Testing-Game/2DGP Game Source File/Map/Tile Map 1.png")

# 캐릭터의 스탠딩 상 하 좌 우 상좌 상우 하좌 하우
character_standing = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_up.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_down.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_left.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_right.png")
    ]

# 프레임 설정
frame = 0

# 캐릭터의 달리기
character_running = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Up_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Down_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Left_Run.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Run/Character_Right_Run.png")
    ]



# 캐릭터 달리기 스프라이트를 쪼개 담을 리스트 선언
rects1 = []
rects2 = []

for i in range(len(character_running)):
    list = []
    rects1.append(character_running[i].get_rect())

    for j in range(4):
        list.append(pygame.Rect(64 * (j + 1), 0, rects1[i].width // 4, rects1[i].height))

    rects2.append(list)

# 캐릭터의 공격
character_attacking = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashUpRight.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashDownLeft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashUPLeft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashDownRight.png")
    ]

# 캐릭터 공격 스프라이트를 쪼개 담을 리스트 선언
attack_rect1 = []
attack_rect2 = []

for i in range(len(character_attacking)):
    list = []
    attack_rect1.append(character_attacking[i].get_rect())

    for j in range(5):
        list.append(pygame.Rect(64 * (j + 1), 0, attack_rect1[i].width // 4, attack_rect1[i].height))

    attack_rect2.append(list)

# 무기의 공격
weapon_attacking = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Weapon_Attack_animation/Sword_UpRight.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Weapon_Attack_animation/Sword_DownLeft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Weapon_Attack_animation/Sword_UPLeft.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Weapon_Attack_animation/Sword_DownRight.png")
    ]

# 무기 공격 스프라이트를 쪼개 담을 리스트 선언

weapon_rect1 = []
weapon_rect2 = []

for i in range(len(weapon_attacking)):
    list = []
    weapon_rect1.append(weapon_attacking[i].get_rect())

    for j in range(5):
        list.append(pygame.Rect(96 * (j + 1), 0, weapon_rect1[i].width // 5, weapon_rect1[i].height))

    weapon_rect2.append(list)

attack_frame = 0

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

# 거미 스탠딩 모션을 담을 리스트
Spider_standing = \
    [
        Spider_standing_up,
        Spider_standing_front,
        Spider_standing_left,
        Spider_standing_right
    ]

