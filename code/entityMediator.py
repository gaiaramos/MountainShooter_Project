#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:

    #Verifica colisão no fim da janela
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    #Verifica as colisões das entidades
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    #Verifica a vida da entidade
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)