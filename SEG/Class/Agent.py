import math
import random

from SEG.config import settings
from SEG.state import state
from SEG.utils.color import speed_to_color


class Agent:
    def __init__(self, x, y, speed, color, chloroplast, parent_id=None, birth_tick=0):
        self.id = state.agents_id_counter
        state.agents_id_counter += 1
        self.parent_id = parent_id

        self.x = x
        self.y = y

        self.energy = 100

        # self.herbivory = herbivory # Травоядность
        # self.carnivorous = carnivorous # Мясоядность
        self.chloroplast = chloroplast  # Хлоропласты

        self.speed = speed
        self.color = color

        self.age = 0
        self.birth_tick = birth_tick
        self.death_tick = None

    def move(self):
        if state.foods and self.speed >= 0:
            nearest_food = min(state.foods, key=lambda f: (self.x - f.x) ** 2 + (self.y - f.y) ** 2)
            dx, dy = nearest_food.x - self.x, nearest_food.y - self.y
            dist = max((dx ** 2 + dy ** 2) ** 0.5, 0.1)
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        self.energy -= (settings.step_energy + self.speed * settings.speed_energy)
        self.age += 1

    def eat(self):
        for food in state.foods:
            if (self.x - food.x) ** 2 + (self.y - food.y) ** 2 < 100:
                self.energy += food.energy
                state.foods.remove(food)
                break
        if self.chloroplast > 0:
            self.energy += settings.chloroplast_energy * self.chloroplast * settings.illumination

    def reproduce(self):
        if self.energy >= settings.div_energy * 1.5 and len(state.agents) < settings.max_agents:
            self.energy -= settings.div_energy

            new_speed = max(-5, min(settings.max_speed,
                                     self.speed + random.uniform(-settings.mut_ratio, settings.mut_ratio)))
            new_chloroplast = max(settings.min_chloroplast, min(settings.max_chloroplast,
                                                                self.chloroplast + random.uniform(-settings.mut_ratio,
                                                                                                  settings.mut_ratio)))
            new_color = speed_to_color(new_speed, settings.max_speed, chloroplast=new_chloroplast)

            child = Agent(self.x, self.y, new_speed, new_color, parent_id=self.id,
                          birth_tick=state.current_tick, chloroplast=new_chloroplast)
            state.all_agents[child.id] = child
            state.agents.append(child)

    def resolve_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.hypot(dx, dy)
        min_dist = 6

        if 0 < dist < min_dist:
            overlap = min_dist - dist
            nx = dx / dist
            ny = dy / dist

            self.x -= nx * overlap / 2
            self.y -= ny * overlap / 2
            other.x += nx * overlap / 2
            other.y += ny * overlap / 2

        elif dist == 0:
            # полностью совпали координатами — рандомно раздвигаем
            min_dist = 13
            offset = min_dist / 2
            angle = random.uniform(0, 2 * math.pi)
            self.x += math.cos(angle) * offset
            self.y += math.sin(angle) * offset
            other.x -= math.cos(angle) * offset
            other.y -= math.sin(angle) * offset
