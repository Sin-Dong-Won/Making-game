import pygame

background1 = pygame.image.load("2DGP Game Source File/Map/Tile Map Test.png")

background1_size = background1.get_rect()
background1_size.width = background1_size.width
background1_size.height = background1_size.height

inventory = pygame.image.load("2DGP Game Source File/Item/Inventory.png")

# 캐릭터의 스탠딩 상 하 좌 우 상좌 상우 하좌 하우
character_standing = \
    [
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_up.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_down.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_left.png"),
        pygame.image.load("2DGP Game Source File/Character/Character_Standing/character_standing_right.png")
    ]

# 캐릭터의 이미지 크기
character_size = character_standing[0].get_rect()
character_size.width = character_size.width
character_size.height = character_size.height

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

# 캐릭터의 체력
character_health = pygame.image.load("2DGP Game Source File/Character/Character_Health/StaticHeart.png")

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

# 거미 사이즈
spider = pygame.image.load("2DGP Game Source File/Monster/SpiderPack/IdleOrange/SpiderIdleDown1.png")
spider_size = spider.get_rect()

spider_width = spider_size.width
spider_height = spider_size.height

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

# Oconid 사이즈
oconid = pygame.image.load("2DGP Game Source File/Monster/Oconid/Oconide_Move/hue-shift-octonid_Down.png")
oconid_size = oconid.get_rect()
oconid_size.width = oconid_size.width // 8

oconid_width = oconid_size.width
oconid_height = oconid_size.height

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
Plant = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Down (1).png")
    ]

Plant_rect1 = []
Plant_rect2 = []

plant = pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (1).png")
plant_size = plant.get_rect()
plant_size_width = plant_size.width // 14
plant_size_height = plant_size.height

for i in range(len(Plant)):
    list = []
    Plant_rect1.append(Plant[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(96 * j, 0, Plant_rect1[i].width // 14, Plant_rect1[i].height))

    Plant_rect2.append(list)

Plant_Attack = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (2).png"),
        pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Down (2).png")
    ]

Plant_Attack_rect1 = []
Plant_Attack_rect2 = []

plant_attack = pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Slice_Up (2).png")
plant_attack_size = plant_attack.get_rect()
plant_attack_size_width = plant_attack_size.width // 14
plant_attack_size_height = plant_attack_size.height

for i in range(len(Plant_Attack)):
    list = []
    Plant_Attack_rect1.append(Plant_Attack[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(96 * j, 0, Plant_Attack_rect1[i].width // 14, Plant_Attack_rect1[i].height))

    Plant_Attack_rect2.append(list)

Plant_Peanut = pygame.image.load("2DGP Game Source File/Monster/Plants/Plant_Peanut.png")
Peanut_Rect = Plant_Peanut.get_rect()
Peanut_rect = []

plant_peanut_size = Plant_Peanut.get_rect()
plant_peanut_size_width = plant_peanut_size.width
plant_peanut_size_height = plant_peanut_size.height

for i in range(8):
    Peanut_rect.append(pygame.Rect(32 * i, 0, Peanut_Rect.width // 8, Peanut_Rect.height))

# ============================================================================
# Plant
# ============================================================================

# ============================================================================
# Boss
# ============================================================================

BOSS_Stand = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Standing (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Standing (2).png")
    ]

BOSS_Stand_rect1 = []
BOSS_Stand_rect2 = []

Boss = pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Standing (1).png")
Boss_size = Boss.get_rect()
Boss_size_width = Boss_size.width // 14
Boss_size_height = Boss_size.height

for i in range(len(BOSS_Stand)):
    list = []
    BOSS_Stand_rect1.append(BOSS_Stand[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(490 * j, 0, BOSS_Stand_rect1[i].width // 4, BOSS_Stand_rect1[i].height))

    BOSS_Stand_rect2.append(list)

BOSS_Attack = \
    [
        pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Attack (1).png"),
        pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Attack (1).png")
    ]

BOSS_Attack_rect1 = []
BOSS_Attack_rect2 = []

Boss_attack = pygame.image.load("2DGP Game Source File/Monster/Boss/Slime_Boss Attack (1).png")
Boss_attack_size = Boss_attack.get_rect()
Boss_attack_size_width = Boss_attack_size.width // 14
Boss_attack_size_height = Boss_attack_size.height

for i in range(len(BOSS_Attack)):
    list = []
    BOSS_Attack_rect1.append(BOSS_Attack[i].get_rect())

    for j in range(14):
        list.append(pygame.Rect(490 * j, 0, BOSS_Attack_rect1[i].width // 8, BOSS_Attack_rect1[i].height))

    BOSS_Attack_rect2.append(list)

# 숫자 불러오기

Numbers = \
    [
        pygame.image.load("2DGP Game Source File/Number/Number_0.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_01.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_02.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_03.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_04.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_05.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_06.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_07.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_08.png"),
        pygame.image.load("2DGP Game Source File/Number/Number_09.png")
    ]

# 아이템 불러오기

Character_Coin = pygame.image.load("2DGP Game Source File/Item/StaticCoin.png")
Character_Crystal = pygame.image.load("2DGP Game Source File/Item/StaticGreenCrystal.png")

Character_Potion_Icon = pygame.image.load("2DGP Game Source File/Item/BigHealthPotion_Icon.png")
Character_Crystal_Icon = pygame.image.load("2DGP Game Source File/Item/StaticGreenCrystal_Icon.png")
