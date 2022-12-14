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
play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()