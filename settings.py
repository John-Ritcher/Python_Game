import math
import pygame as pg

# game settings
pg.init()
screen_info = pg.display.Info()
RES = screen_width, screen_height = screen_info.current_w, screen_info.current_h
HALF_WIDTH = screen_width // 2
HALF_HEIGHT = screen_height // 2


FPS = 60

PLAYER_POS = 1.5, 5 # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = screen_width - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = screen_width // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = screen_width // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE= TEXTURE_SIZE // 2