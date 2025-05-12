import random

import pygame

from SEG.config import settings


def init_music(volume=0.5):
    path = random.choice(settings.musics)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)  # -1 — бесконечный цикл

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()
