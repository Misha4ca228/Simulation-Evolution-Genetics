import random

from SEG.state import state
import SEG.config as cfg
from SEG.utils.color import speed_to_color


class Agent:
    def __init__(self, x, y, speed, color, parent_id=None, birth_tick=0):
        self.id = state.agents_id_counter
        state.agents_id_counter += 1

        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.energy = 70
        self.age = 0
        self.parent_id = parent_id
        self.birth_tick = birth_tick
        self.death_tick = None


    def move(self):
        if state.foods:
            nearest_food = min(state.foods, key=lambda f: (self.x - f.x) ** 2 + (self.y - f.y) ** 2)
            dx, dy = nearest_food.x - self.x, nearest_food.y - self.y
            dist = max((dx ** 2 + dy ** 2) ** 0.5, 0.1)
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
        self.energy -= (cfg.step_energy + self.speed * cfg.speed_energy)
        self.age += 1

    def eat(self):
        for food in state.foods:
            if (self.x - food.x) ** 2 + (self.y - food.y) ** 2 < 100:
                self.energy += food.energy
                state.foods.remove(food)
                break

    def reproduce(self):
        if self.energy >= cfg.div_energy * 1.5:
            self.energy -= cfg.div_energy

            new_speed = max(0.5, min(cfg.max_speed, self.speed + random.uniform(-cfg.mut_ratio, cfg.mut_ratio)))
            new_color = speed_to_color(new_speed, cfg.max_speed)
            child = Agent(self.x, self.y, new_speed, new_color, parent_id=self.id,
                             birth_tick=state.current_tick)
            state.all_agents[child.id] = child
            state.agents.append(child)