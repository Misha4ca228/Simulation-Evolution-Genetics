import threading

import pygame
from SEG.config import settings
from SEG.state import state
from SEG.ui.game_info import render_game_info
from SEG.ui.main_tk import main_tk
from SEG.utils.agent import render_agents, init_agent, resolve_all_collisions
from SEG.utils.food import random_spawn_food, render_food, add_food
from SEG.utils.music import init_music


pygame.init()

screen = pygame.display.set_mode(settings.window_size)
pygame.display.set_caption("SEG V2.0 RELEASE!")

background = pygame.Surface(settings.window_size).convert()
background.fill(settings.background_color)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

threading.Thread(target=main_tk, daemon=True).start()

init_music()
init_agent(count=settings.initial_agents)

while state.running:
    screen.blit(background, (0, 0))
    fps = int(clock.get_fps())
    pygame.display.set_caption(f"SEG V2.0 RELEASE! | FPS: {fps}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state.is_pause = not state.is_pause

    render_food(screen, font)
    render_agents(screen, font)
    render_game_info(screen, font)
    pygame.display.flip()

    if state.is_pause:
        continue

    speed_count = 0
    for agent in state.agents[:]:
        agent.move()
        agent.eat()
        agent.reproduce()
        speed_count += agent.speed

        if agent.energy <= 0:
            agent.death_tick = state.current_tick
            state.agents.remove(agent)

        if agent.age >= settings.max_age:
            agent.death_tick = state.current_tick
            state.agents.remove(agent)
            add_food(x=agent.x, y=agent.y, energy=agent.energy, type="death")

    state.avg_speed = round(speed_count / max(1, len(state.agents)), 1)
    resolve_all_collisions(state.agents)

    if state.food_timer >= 1.0:
        random_spawn_food(count=settings.food_per_second)
        state.food_timer = 0

    state.current_tick += 1
    delta_t = 60 / 1000
    state.food_timer += delta_t
    clock.tick(50)

pygame.quit()
