import pygame
import random
import config as cfg
from SEG.state import state
from SEG.ui.game_info import render_game_info
from SEG.utils.agent import render_agents, init_agent
from SEG.utils.food import random_spawn_food, render_food, add_food
from SEG.utils.tree import build_tree


pygame.init()

screen = pygame.display.set_mode(cfg.window_size)
pygame.display.set_caption("SEG v1.0.2")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

init_agent(count=cfg.initial_agents)

while state.running:
    clock.tick(50)
    state.current_tick += 1
    delta_t = 60 / 1000
    state.food_timer += delta_t

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                build_tree()

    speed_count = 0
    for agent in state.agents[:]:
        agent.move()
        agent.eat()
        agent.reproduce()
        speed_count += agent.speed

        if agent.energy <= 0:
            agent.death_tick = state.current_tick
            state.agents.remove(agent)

        if agent.age >= cfg.max_age:
            agent.death_tick = state.current_tick
            state.agents.remove(agent)
            add_food(x=agent.x, y=agent.y, energy=agent.energy, type="death")

    state.avg_speed = round(max(1, speed_count) / max(1, len(state.agents)), 2)

    if state.food_timer >= 1.0:
        random_spawn_food(count=cfg.food_per_second)
        state.food_timer = 0

    screen.fill(cfg.background_color)
    render_food(screen)
    render_agents(screen)
    render_game_info(screen, font)
    pygame.display.flip()


pygame.quit()
