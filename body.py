import numpy as np
import pygame
from config import body_1_color
from contants import G

class Body:

    def __init__(self, m, r, postion, velocity, color=body_1_color, movable=True):
        self.m = m
        self.r = r
        self.position = postion
        self.color = color
        self.velocity = velocity
        self.movable = movable

    def setup_a(self, bodies):
        self.a = np.zeros([2])
        
        for body in bodies:
            if body != self:
                mag_a = G * self.m * body.m / sum(np.square(np.subtract(self.position, body.position)))
                self.a = np.add(self.a, np.multiply(np.subtract(body.position, self.position), mag_a / np.linalg.norm(np.subtract(body.position, self.position))))


    def update(self, dt):
        if self.movable:
            self.velocity = np.add(self.velocity, np.multiply(self.a, dt))
            self.position = np.add(self.position, np.multiply(self.velocity, dt))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [int(x) for x in self.position], int(self.r))