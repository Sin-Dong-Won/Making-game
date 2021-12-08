import pygame
import Setting as Set
import Load_Asset as load

screen = Set.screen

# Character Size

bg_bb_start_x = 84
bg_bb_start_y = 96
bg_width = load.background1_size.width - bg_bb_start_x * 2
bg_height = load.background1_size.height - bg_bb_start_y * 2


class Map:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("2DGP Game Source File/Map/Tile Map Test.png")
        self.boundding_box = self.get_bounding_box()
        self.clear_box = self.get_clear_box()

    # 맵의 바운딩 박스
    def get_bounding_box(self):
        return [self.x + bg_bb_start_x, self.y + bg_bb_start_y, bg_width, bg_height]

    def get_clear_box(self):
        return [bg_width // 2 + 42, self.y + bg_bb_start_y, bg_bb_start_x, bg_bb_start_y // 2]

    def update(self):
        pass

    def draw(self):
        screen.blit(self.image, (0, 0))
        pygame.draw.rect(screen, Set.RED, self.boundding_box, 2)
        pygame.draw.rect(screen, Set.BLUE, self.clear_box, 2)
