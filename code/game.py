#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            size=(WIN_WIDTH, WIN_HEIGHT))  # Cria a janela (ctrl+alt+l organiza o código)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[4]]:
                player_score = [0, 0]  # [Player1, Player3]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

            # Entrar nos Levels individuais
            #elif menu_return == MENU_OPTION[1]: # Entra no Level1
                #player_score = [0, 0]
                #level = Level(self.window, 'Level1', menu_return, player_score)
                #level_return = level.run(player_score)
                #if level_return:
                    #score.save()
            #elif menu_return == MENU_OPTION[2]: # Entra no Level2
                #player_score = [0, 0]
                #level = Level(self.window, 'Level2', menu_return, player_score)
                #level_return = level.run(player_score)
                #if level_return:
                    #score.save()
            #elif menu_return == MENU_OPTION[3]:  # Entra no Level3
                #player_score = [0, 0]
                #level = Level(self.window, 'Level3', menu_return, player_score)
                #level_return = level.run(player_score)
                #if level_return:
                    #score.save()

            elif menu_return == MENU_OPTION[5]:  # Mostra o Score
                score.show()
            elif menu_return == MENU_OPTION[6]:
                pygame.quit()
            quit()  # end pygamne
        else:
            pygame.quit()
