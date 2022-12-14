import pygame
from PIL import Image
from random import randint

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32
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
class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        window.blit(imgBrick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            objects.remove(self)
objects = []
for _ in range(50):
    while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect): fined = True

        if not fined: break

    Block(x, y, TILE)
play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    for obj in objects: obj.update()
    window.fill((0, 0, 0))
    for obj in objects: obj.draw()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()