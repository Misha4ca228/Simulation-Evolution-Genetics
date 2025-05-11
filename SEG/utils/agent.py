import random

import pygame

import SEG.config as cfg
from SEG.Class.Agent import Agent
from SEG.state import state
from SEG.utils.color import speed_to_color

width, height = cfg.window_size



def init_agent(count=1):
    for i in range(count):
        init_speed = random.uniform(1, 4)
        init_color = speed_to_color(init_speed, max_speed=cfg.max_speed)
        agent = Agent(x=random.randint(0, width), y=random.randint(0, height), speed=init_speed, color=init_color)
        state.agents.append(agent)
        state.all_agents[agent.id] = agent


def render_agents(screen):
    for agent in state.agents:
        pygame.draw.circle(screen, agent.color, (agent.x, agent.y), 5)