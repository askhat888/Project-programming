import pygame
from PIL import Image
from random import randint

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")
fontUI = pygame.font.Font(None, 30)
fontRes = pygame.font.Font(None, 24)
imgBrick = pygame.image.load('block_brick.png')
imgTanks = [
    pygame.image.load('tank1.png'),
    pygame.image.load('tank2.png'),
    pygame.image.load('tank3.png'),
    pygame.image.load('tank4.png'),
    pygame.image.load('tank5.png'),
    pygame.image.load('tank6.png'),
    pygame.image.load('tank7.png'),
    pygame.image.load('tank8.png'),
]
imgBangs = [
    pygame.image.load('bang1.png'),
    pygame.image.load('bang2.png'),
    pygame.image.load('bang3.png'),
]
play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()