# Cores
import pygame

from code.entity import Entity

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 2,
    #'Player3': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 2,
    'Enemy2Shot': 2,
}

#Times
ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Player1': 100,
    'Player2': 200,

}

# Player
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

#Health
ENTITY_HEALTH = {
    'LevelBg0' : 999,
    'LevelBg1': 999,
    'LevelBg2': 999,
    'LevelBg3': 999,
    'LevelBg4': 999,
    'LevelBg5': 999,
    'LevelBg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,

}

# Definição perfil
MENU_OPTION = ('NEW GAME',
               'LEVEL 1',
               'LEVEL 2',
               'LEVEL 3',
               'SCORE',
               'EXIT')

# Spawn
SPAWN_TIME = 4000

# Tamanhos
WIN_WIDTH = 576
WIN_HEIGHT = 324

