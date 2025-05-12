import random

import pygame

from SEG.Class.Food import Food
import SEG.config as cfg
from SEG.config import settings
from SEG.state import state

width, height = settings.window_size


def add_food(x, y, energy, type):
    food = Food(x=x, y=y, energy=energy, type=type)
    state.foods.append(food)


def random_spawn_food(count=10):
    if state.food_timer >= 1:
        state.food_timer = 0
        for i in range(count):
            if not len(state.foods) <= settings.max_food:
                break
            add_food(x=random.randint(0, width), y=random.randint(0, height),
                     energy=random.randint(settings.min_food_energy, settings.max_food_energy),
                     type=random.choice(["plaint", "meat"]))


def render_food(screen):
    for food in state.foods:
        pygame.draw.circle(screen, food.color, (food.x, food.y), food.size)
