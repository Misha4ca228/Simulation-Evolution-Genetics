import tkinter as tk

from SEG.config import settings
from SEG.ui.tk_state import tk_state


def create_entry(label_text, attr_name, window):
    frame = tk.Frame(window)
    frame.pack(pady=5, fill="x")

    label = tk.Label(frame, text=label_text)
    label.pack(side="left", padx=5)

    entry = tk.Entry(frame)
    entry.insert(0, str(getattr(settings, attr_name)))
    entry.pack(side="right", expand=True, fill="x", padx=5)

    tk_state.entries[attr_name] = entry

def save_settings():
    for attr, entry in tk_state.entries.items():
        value_str = entry.get()
        current_value = getattr(settings, attr)

        try:
            # Попробуем привести к float
            value = float(value_str)
            # Если в settings атрибут был int — и float без дробной части, кастуем в int
            if isinstance(current_value, int) and value.is_integer():
                value = int(value)
        except ValueError:
            print(f"Ошибка преобразования поля '{attr}': {value_str}")
            continue  # Пропускаем, если не удалось преобразовать

        setattr(settings, attr, value)

