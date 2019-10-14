import pygame
from config import *
import sys

pygame.init()

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Three Body Problem')

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(background_color)
    pygame.draw.circle(surface, body_1_color, [200, 200], 10)

    pygame.display.flip()