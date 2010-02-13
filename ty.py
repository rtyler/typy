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
    parent_width = None
    parent_height = None

    def __init__(self, parent, **kwargs):
        self.__dict__.update(kwargs)
        self.parent = parent
        self.parent_width, self.parent_height = parent.get_size()
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

        buffer = ''.join(self.spooled)
        spool_width, spool_height = self.font.size(buffer)
        offset_y = self.parent_height - (5 + spool_height)
        offset_x = (self.parent_width / 2) - (spool_width / 2)
        self.parent.blit(self.font.render(buffer, 0, self.color),
                (offset_x, offset_y,))

class AnimatingObject(object):
    surface = None
    parent = None
    width, height = None, None
    parent_width, parent_height = None, None

    def update(self):
        ''' Return True if the object is offscreen '''
        pass

class AnimatingWord(AnimatingObject):
    color = (255, 255, 255,)
    word = None
    font = None
    step = 0.05
    offset_x, offset_y = None, None

    def __init__(self, parent, word, **kwargs):
        self.__dict__.update(kwargs)
        self.parent = parent
        self.parent_width, self.parent_height = parent.get_size()
        self.word = word
        self.font = pygame.font.SysFont('Courier', 42)

        self.width, self.height = self.font.size(word)
        self.offset_x = self.parent_width
        self.offset_y = (self.parent_height / 2) - (self.height / 2)
        self.surface = self.font.render(word, 0, self.color)

    def is_offscreen(self):
        return False

    def update(self):
        ''' Update the word's position, returning True if it's offscreen '''
        self.parent.fill( (0, 0, 0),
                rect=pygame.Rect(self.offset_x, self.offset_y,
                    self.width, self.height))
        self.parent.blit(self.surface, (self.offset_x, self.offset_y))
        self.offset_x = self.offset_x - self.step
        return False


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

        words = [AnimatingWord(self.surface, 'Hello')]
        while run:
            for event in pygame.event.get():
                run = self.handle_event(event)

            for w in words:
                w.update()

            pygame.display.update()
        if self.background_music:
            pygame.mixer.music.stop()

if __name__ == "__main__" :
    pygame.init()
    typy = Typy(640, 480)
    typy.runloop()
    pygame.quit()
