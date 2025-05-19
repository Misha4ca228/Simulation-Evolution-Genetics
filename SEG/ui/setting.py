import tkinter as tk


def settings_window(window):


    scale = tk.Scale(window, from_=0, to=100, orient="horizontal", label="Выберите значение")
    scale.pack(pady=10)

    save_button = tk.Button(window, text="Сохранить настройки")
    save_button.pack(pady=10)

    cancel_button = tk.Button(window, text="Отменить")
    cancel_button.pack(pady=10)
