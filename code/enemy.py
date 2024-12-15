#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.enemyShot import EnemyShot
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        if self.name == 'Enemy3':
            self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade vertical inicial
            self.moving_down = True  # Controle de movimento Enemy3

    def move(self):
        # Movimento horizontal padrão
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento especial Enemy3
        if self.name == 'Enemy3':
            if self.moving_down:
                self.rect.centery += self.vertical_speed
                if self.rect.bottom >= WIN_HEIGHT:  # Verifica se atingiu a borda inferior
                    self.moving_down = False
            else:
                self.rect.centery -= self.vertical_speed
                if self.rect.top <= 0:  # Verifica se atingiu a borda superior
                    self.moving_down = True
                    self.vertical_speed *= 2  # Dobra a velocidade ao descer
                elif self.vertical_speed > ENTITY_SPEED[self.name]:
                    self.vertical_speed = ENTITY_SPEED[self.name]  # Restaura a velocidade padrão

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))