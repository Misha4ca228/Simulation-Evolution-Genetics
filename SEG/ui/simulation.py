from SEG.utils.tk_utils import create_entry, save_settings
import tkinter as tk

def simulation_window(window):
    create_entry("Частота спавна еды Еда/сек ", "food_per_second", window)
    create_entry("Максимальный возраст агента", "max_age", window)
    create_entry("Максимальная скорость", "max_speed", window)
    create_entry("Минимальная энергия еды ", "min_food_energy", window)
    create_entry("Максимальная энергия еды", "max_food_energy", window)
    create_entry("Максимальное кол-во еды ", "max_food", window)
    create_entry("Максимальное кол-во агентов", "max_agents", window)
    create_entry("Сила мутации", "mut_ratio", window)
    create_entry("Энергия необходимая для деления", "div_energy", window)
    create_entry("Базовая трата энергия за шаг", "step_energy", window)
    create_entry("Множитель энергии за скорость", "speed_energy", window)

    save_button = tk.Button(window, text="Сохранить настройки симуляции", command=save_settings)
    save_button.pack(pady=50)