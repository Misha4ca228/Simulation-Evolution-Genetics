from SEG.config import settings
from SEG.state import state
import SEG.config as cfg

def render_game_info(screen, font):
    lines = [
        f"Еда: {len(state.foods)}/{settings.max_food}",
        f"Агенты: {len(state.agents)}/{settings.max_agents}",
        f"Год: {state.current_tick // settings.ticks_per_year}",
        f"Ср.Скорость: {state.avg_speed}"
    ]
    y = 10
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (10, y))
        y += font.get_height() + 5  # отступ между строками
