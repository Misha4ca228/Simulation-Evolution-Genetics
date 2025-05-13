class Settings:
    def __init__(self):
        self.initial_agents = 1  # Начальная популяция
        self.food_per_second = 15  # Появление еды еда\сек
        self.ticks_per_year = 100  # 1 игровой год
        self.window_size = (800, 800)  # Размекры окна
        # Гены
        self.mut_ratio = 0.15  # Сила смутации
        # Энергия
        self.div_energy = 80  # Энергия необходимая для деления
        self.step_energy = 0.1 # Энергия расходуемая за 1 шаг
        self.speed_energy = 0.1  # Множитель энергии расходуемой скоростью energy - speed / 2 *speed_energy
        # Ограничения
        self.max_age = 1000  # МаксимальныЙ возраст
        self.max_speed = 10.0  # Максимальная скорость
        self.min_food_energy = 30  # Минимальная энергия еды
        self.max_food_energy = 50  # Максимальная энергия еды
        self.max_food = 200  # Максимальное кол-во еды на поле
        self.max_agents = 100
        # Цвета
        self.background_color = (48, 54, 64)  # Цвет фона
        # Музыка
        self.musics = [
            "resources/musics/1.ogg"
        ]


settings = Settings()
