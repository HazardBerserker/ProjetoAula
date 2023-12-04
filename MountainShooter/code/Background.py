#!/usr/bin/python
# -*- coding: utf-8 -*-
from MountainShooter.code.Const import WIN_WIDTH, ENTITY_SPEED
from MountainShooter.code.Entity import Entity


class Background(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
