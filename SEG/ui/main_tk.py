import tkinter as tk
from tkinter import ttk
from SEG.config import settings  # Импорт текущих настроек
from SEG.ui.simulation import simulation_window
from SEG.ui.tk_state import tk_state
from SEG.ui.tree import tree_window
from SEG.utils.tk_utils import create_entry


def main_tk():
    window = tk.Tk()
    window.title("SEG V2.0 RELEASE!")
    window.geometry("400x600")
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)

    main = ttk.Frame(notebook)
    sim = ttk.Frame(notebook)
    agent = ttk.Frame(notebook)
    tree = ttk.Frame(notebook)
    setting = ttk.Frame(notebook)

    #notebook.add(main, text='Главная')
    notebook.add(sim, text='Симуляция')
    #notebook.add(agent, text='Агент')
    notebook.add(tree, text='Древо')
    #notebook.add(setting, text='Настройки')

    simulation_window(sim)
    tree_window(tree)

    window.mainloop()

