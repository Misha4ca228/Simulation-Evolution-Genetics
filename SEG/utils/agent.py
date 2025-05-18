import random

import pygame
from SEG.Class.Agent import Agent
from SEG.config import settings
from SEG.state import state
from SEG.ui.agent import draw_agent_info
from SEG.utils.color import speed_to_color

width, height = settings.window_size


def init_agent(count=1):
    for i in range(count):
        init_speed = random.uniform(1, 1.5)
        init_color = speed_to_color(init_speed, max_speed=settings.max_speed)
        agent = Agent(x=random.randint(0, width), y=random.randint(0, height), speed=init_speed, color=init_color)
        state.agents.append(agent)
        state.all_agents[agent.id] = agent


def render_agents(screen, font):
    mouse_pos = pygame.mouse.get_pos()
    hovered_agents = [
        (agent, (agent.x - mouse_pos[0]) ** 2 + (agent.y - mouse_pos[1]) ** 2)
        for agent in state.agents
        if is_mouse_over_agent(agent, mouse_pos)
    ]

    closest_agent = min(hovered_agents, key=lambda t: t[1])[0] if hovered_agents else None

    for agent in state.agents:
        pygame.draw.circle(screen, agent.color, (agent.x, agent.y), 6)

    if closest_agent:
        draw_agent_info(screen, closest_agent, mouse_pos, font)


def resolve_all_collisions(agents):
    for i in range(len(agents)):
        for j in range(i + 1, len(agents)):
            agents[i].resolve_collision(agents[j])

def is_mouse_over_agent(agent, mouse_pos):
    dx = agent.x - mouse_pos[0]
    dy = agent.y - mouse_pos[1]
    return dx * dx + dy * dy <= 4 * 4

