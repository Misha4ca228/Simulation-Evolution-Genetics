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
        value = entry.get()
        current_value = getattr(settings, attr)

        if isinstance(current_value, int):
            value = int(value)
        elif isinstance(current_value, float):
            value = float(value)

        setattr(settings, attr, value)

