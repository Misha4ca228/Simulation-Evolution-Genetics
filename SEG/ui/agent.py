
def draw_agent_info(screen, agent, pos, font):
    lines = [
        f"ID: {agent.id}",
        f"Speed: {agent.speed:.2f}",
        f"Energy: {agent.energy:.1f}",
        f"Age: {agent.age}",
    ]
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (pos[0] + 10, pos[1] + 15 * i))
