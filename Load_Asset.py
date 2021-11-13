import pygame

background1 = pygame.image.load("2DGP Game Source File/Map/Tile Map Test.png")
inventory = pygame.image.load("2DGP Game Source File/Item/Inventory.png")

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
        list.append(pygame.Rect(64 * (j), 0, rects1[i].width // 4, rects1[i].height))

    rects2.append(list)

# 캐릭터의 공격
character_attacking = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashUpRight_Fix.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashDownLeft_Fix.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashUPLeft_Fix.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Attack/Character_Attack_animation/Character_SlashDownRight_Fix.png")
    ]

# 캐릭터 공격 스프라이트를 쪼개 담을 리스트 선언
attack_rect1 = []
attack_rect2 = []

for i in range(len(character_attacking)):
    list = []
    attack_rect1.append(character_attacking[i].get_rect())

    for j in range(5):
        list.append(pygame.Rect(64 * (j), 0, attack_rect1[i].width // 5, attack_rect1[i].height))

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
        list.append(pygame.Rect(96 * (j), 0, weapon_rect1[i].width // 5, weapon_rect1[i].height))

    weapon_rect2.append(list)

attack_frame = 0

# 적 설정


# 거미 스탠딩

Spider_standing_up = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleUp4.png")
    ]

Spider_standing_down = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleDown1.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleDown2.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleDown3.png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleDown4.png")
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
        Spider_standing_down,
        Spider_standing_left,
        Spider_standing_right
    ]

# 거미 걷기

Spider_walking_up = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingUp (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingUp (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingUp (3).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingUp (4).png")
    ]

Spider_walking_down = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingDown (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingDown (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingDown (3).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingDown (4).png")
    ]

Spider_walking_left = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingLeft (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingLeft (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingLeft (3).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingLeft (4).png")
    ]

Spider_walking_right = \
    [
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingRight (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingRight (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingRight (3).png"),
        pygame.image.load("2DGP Game Source File/Monster/SpiderPack/WalkingOrange/SpiderWalkingRight (4).png")
    ]

# 거미 걷기 모션을 담을 리스트
Spider_walking = \
    [
        Spider_walking_up,
        Spider_walking_down,
        Spider_walking_left,
        Spider_walking_right
    ]
# ============================================================================
# Oconid
# ============================================================================
Oconid = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Oconid/Oconide_Move/hue-shift-octonid_Up.png"),
        pygame.image.load("2DGP Game Source File/Monster/Oconid/Oconide_Move/hue-shift-octonid_Down.png"),
        pygame.image.load("2DGP Game Source File/Monster/Oconid/Oconide_Move/hue-shift-octonid_Left.png"),
        pygame.image.load("2DGP Game Source File/Monster/Oconid/Oconide_Move/hue-shift-octonid_Right.png")
    ]

oconid_rect1 = []
oconid_rect2 = []

for i in range(len(Oconid)):
    list = []
    oconid_rect1.append(Oconid[i].get_rect())

    for j in range(8):
        list.append(pygame.Rect(96 * (j), 0, oconid_rect1[i].width // 8, oconid_rect1[i].height))

    oconid_rect2.append(list)

oconid_frame = 0
# ============================================================================
# Oconid
# ============================================================================

# ============================================================================
# Plant
# ============================================================================
Plant =  \
    [
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Down (1).png")
    ]

Plant_rect1 = []
Plant_rect2 = []

for i in range(len(Plant)):
    list = []
    Plant_rect1.append(Plant[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(96 * (j), 0, Plant_rect1[i].width // 14, Plant_rect1[i].height))

    Plant_rect2.append(list)

Plant_Attack = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Down (2).png")
    ]

Plant_Attack_rect1 = []
Plant_Attack_rect2 = []

for i in range(len(Plant_Attack)):
    list = []
    Plant_Attack_rect1.append(Plant_Attack[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(96 * (j), 0, Plant_Attack_rect1[i].width // 14, Plant_Attack_rect1[i].height))

    Plant_Attack_rect2.append(list)

Plant_Peanut = pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Peanut.png")
Peanut_Rect = Plant_Peanut.get_rect()
Peanut_rect = []

for i in range(8):
    Peanut_rect.append(pygame.Rect(32 * (i), 0, Peanut_Rect.width // 8, Peanut_Rect.height))
# ============================================================================
# Plant
# ============================================================================