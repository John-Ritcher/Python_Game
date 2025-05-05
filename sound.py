import pygame as pg
from random import shuffle, choice
import os

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.mp3_files = [file for file in os.listdir(self.path) if file.endswith('.mp3')]
        self.random_mp3 = choice(self.mp3_files)
        file_path = os.path.join(self.path, self.random_mp3)
        pg.mixer.music.load(file_path)
        pg.mixer.music.set_volume(0.3)