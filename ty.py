#!/usr/bin/env python

import logging
import os
import sys
import random

import pygame
from pygame.locals import *

from typy import words

if os.environ.get('DEBUG'):
    logging.basicConfig(level=logging.DEBUG)

class LetterSpool(object):
    spooled = None
    parent = None
    font = None
    clear_keys = (K_RETURN, K_SPACE,)
    color = (255, 255, 255,)

    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.font = pygame.font.SysFont('Courier', 32)
        self.spooled = []

    def clear(self):
        logging.debug('LetterSpool.clear()')
        self.spooled = []

    def handle_key(self, event):
        if event.key in self.clear_keys:
            self.clear()
            return
        if event.key == K_BACKSPACE:
            self.spooled = self.spooled[:-1]
        else:
            self.spooled.append(event.unicode)
        self.parent.blit(self.font.render(''.join(self.spooled), 0, self.color),
                (0,0,))


class Typy(object):
    surface = None
    size = None
    clock = None
    tick = 15
    background_music = False
    font = None
    spool = None
    current_letters = None

    def __init__(self, width, height, **kwargs):
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size,
                pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.clock = pygame.time.Clock()
        self.clock.tick(self.tick)
        pygame.display.set_caption('Typy!')
        pygame.mouse.set_visible(False)

        self.font = pygame.font.SysFont('Courier', 48)
        self.spool = LetterSpool(self.surface)

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
            self.spool.handle_key(event)
        print ('handle_event', event)
        return True

    def runloop(self):
        run = True
        if self.background_music:
            pygame.mixer.music.load('background.mid')
            pygame.mixer.music.play(-1, 0.0)

        word_x = 480
        step = 0.05
        text = 'hello'
        word = self.font.render(text, 0, (255,255,255))
        f_w, f_h = self.font.size(text)
        off_screen = len(text) * f_w
        while run:
            for event in pygame.event.get():
                run = self.handle_event(event)

            if word_x >= -off_screen:
                # Rect(left, top, width, height)
                self.surface.fill((0,0,0), 
                        rect=pygame.Rect(word_x, 100, f_w, f_h))
                self.surface.blit(word, (word_x, 100))
                word_x = word_x - step

            pygame.display.update()
        pygame.mixer.music.stop()

if __name__ == "__main__" :
    pygame.init()
    typy = Typy(640, 480)
    typy.runloop()
    pygame.quit()
