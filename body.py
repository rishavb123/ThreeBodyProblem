from util import mod_pos
import numpy as np
import pygame
from config import body_1_color
from contants import G

class Body:

    min_r = 100
    num_updates = 10

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
                r_squared = sum(np.square(np.subtract(self.position, body.position)))
                if r_squared < Body.min_r:
                    r_squared = Body.min_r
                mag_a = G *body.m / r_squared
                self.a = np.add(self.a, np.multiply(np.subtract(body.position, self.position), mag_a / np.linalg.norm(np.subtract(body.position, self.position))))
            for body2 in bodies:
                diff = np.subtract(body.position, body2.position)
                dist = np.linalg.norm(diff)
                if body != body2 and dist < 10:
                    body.velocity = -np.array(body.velocity)
                    body2.velocity = -np.array(body2.velocity)


    def update(self, dt):
        for _ in range(Body.num_updates):
            if self.movable:
                self.velocity = np.add(self.velocity, np.multiply(self.a, dt / Body.num_updates))
                self.position = np.add(self.position, np.multiply(self.velocity, dt / Body.num_updates))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, mod_pos([int(x) for x in self.position]), int(self.r))