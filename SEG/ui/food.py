def draw_food_info(screen, food, pos, font):
    lines = [
        f"Type: {food.type}",
        f"Energy: {food.energy:.1f}",
    ]
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (pos[0] + 10, pos[1] + 15 * i))
