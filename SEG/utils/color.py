def speed_to_color(speed, max_speed):
    ratio = speed / max_speed
    red = int(255 * ratio)
    blue = int(255 * (1 - ratio))
    green = 50
    return (red, green, blue)