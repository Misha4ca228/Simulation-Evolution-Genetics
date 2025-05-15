def speed_to_color(speed, max_speed, chloroplast):
    # Защита от деления на ноль
    if max_speed == 0:
        ratio = 0
    else:
        ratio = max(0, min(speed / max_speed, 1))  # Clamp в диапазон [0, 1]

    # Красный и синий по скорости
    red = int(255 * ratio)
    blue = int(255 * (1 - ratio))

    # Зелёный по хлоропласту
    if chloroplast <= 0:
        green = 0
    else:
        green = int(min(1, chloroplast) * 255)  # Clamp до 1

    # Убедимся, что все значения находятся в [0, 255]
    red = max(0, min(255, red))
    green = max(0, min(255, green))
    blue = max(0, min(255, blue))

    return (red, green, blue)