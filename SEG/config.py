# Параметры
initial_agents = 1 # Начальная популяция
food_per_second = 3  # Появление еды еда\сек
ticks_per_year = 100  # 1 игровой год
window_size = (800, 800)

# Гены
mut_ratio = 0.1

# Энергия
div_energy = 70
step_energy = 0.1
speed_energy = 0.2

# Ограничения
max_age = 1000  # Максимальные возраст
max_speed = 10.0  # Максимальная скорость
min_food_energy = 30  # Минимальная энергия еды
max_food_energy = 45  # Максимальная энергия еды
max_food = 190

# Цвета
background_color = (48, 54, 64)


class Settings:
    def __init__(self):
        self.initial_agents = 1  # Начальная популяция
        self.food_per_second = 10  # Появление еды еда\сек
        self.ticks_per_year = 100  # 1 игровой год
        self.window_size = (800, 800)  # Размекры окна
        # Гены
        self.mut_ratio = 0.1  # Сила смутации
        # Энергия
        self.div_energy = 70  # Энергия необходимая для деления
        self.step_energy = 0.2  # Энергия расходуемая за 1 шаг
        self.speed_energy = 0.4  # Множитель энергии расходуемой скоростью energy - speed*speed_energy
        # Ограничения
        self.max_age = 1000  # МаксимальныЙ возраст
        self.max_speed = 10.0  # Максимальная скорость
        self.min_food_energy = 30  # Минимальная энергия еды
        self.max_food_energy = 40  # Максимальная энергия еды
        self.max_food = 190  # Максимальное кол-во еды на поле
        # Цвета
        self.background_color = (48, 54, 64)  # Цвет фона


settings = Settings()
