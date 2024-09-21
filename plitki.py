import pygame
import os
import sys
current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()


on_image = pygame.image.load('data/image/on.png').convert_alpha()
of_image = pygame.image.load('data/image/of.png').convert_alpha()
p_1_image = pygame.image.load('data/image/p_1.png').convert_alpha()
p_2_image = pygame.image.load('data/image/p_2.png').convert_alpha()



plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

list_player = []

NUM_HOD = 0

font = pygame.font.SysFont('aria',40)

maps_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]


def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()


class Plitka(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.on = True
        self.adr = (self.rect.y // 100, self.rect.x //100)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)




