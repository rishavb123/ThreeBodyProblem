import pygame
from config import *
import sys
from body import Body
import time
from contants import *

pygame.init()

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Three Body Problem')

clock = pygame.time.Clock()

bodies = [Body(10, 10, [300, 100], [0, 300], body_1_color), Body(10, 10, [500, 100], [-100, 0], body_2_color)]
# bodies = [Body(10, 10, [100, 500], [0, 0], body_1_color), Body(10, 10, [500, 500], [0, 0], body_2_color), Body(10, 10, [300, 100], [0, 0], body_3_color)]
# bodies = [Body(100, 30, [400, 300], [0, 0], body_1_color, False), Body(10, 10, [400, 50], [600, 0], body_2_color)]

current_time = time.time()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(background_color)

    dt = time.time() - current_time

    for body in bodies:
        body.setup_a(bodies)
        body.update(dt)
        body.draw(surface)

    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            pygame.draw.line(surface, BLACK, bodies[i].position, bodies[j].position)

    current_time += dt
    pygame.display.flip()