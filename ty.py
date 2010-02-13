#!/usr/bin/env python

import sys
import random

import pygame
from pygame.locals import *

class ExitException(Exception):
    pass

class Typy(object):
    surface = None
    size = None
    clock = None
    tick = 30
    background_music = False
    font = None

    def __init__(self, width, height, **kwargs):
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size,
                pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.clock.tick(self.tick)
        pygame.display.set_caption('Typy!')
        pygame.mouse.set_visible(False)

        self.font = pygame.font.SysFont('Courier', 48)

    def should_exit(self, event):
        if event.type == QUIT:
            return True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
        return False

    def handle_event(self, event):
        ## Return a boolean whether we should continue the runloop
        if self.should_exit(event):
            return False
        if event.type == KEYDOWN:
            self.surface.fill((0, 0, 0))
            self.surface.blit(self.font.render(event.unicode, 0, (255,255,255)),
                    (0,0))
        print ('handle_event', event)
        return True

    def runloop(self):
        if self.background_music:
            pygame.mixer.music.load('background.mid')
            pygame.mixer.music.play(-1, 0.0)
        run = True
        while run:
            for event in pygame.event.get():
                run = self.handle_event(event)
            pygame.display.update()
        pygame.mixer.music.stop()

if __name__ == "__main__" :
    pygame.init()
    typy = Typy(640, 480)
    typy.runloop()
    pygame.quit()
