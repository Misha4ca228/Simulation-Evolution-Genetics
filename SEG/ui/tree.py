import tkinter as tk
from tkinter import filedialog

from SEG.utils.tree import build_tree


def tree_window(window):
    save_button = tk.Button(window, text="Сохранить древо", command=build_tree)
    save_button.pack(pady=50)
