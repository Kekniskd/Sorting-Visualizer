from random import randint, choice
from ttkbootstrap import ttk
import tkinter as tk


class Bar:
    def __init__(self, master: tk.Tk, win_height: int) -> None:
        B_STYLE = choice(['primary', 'secondary', 'success', 'info', 'warning', 'danger', 'dark'])
        height = randint(1, 100)
        height_pct = height / 100
        self.bar_height = round(height_pct * win_height) - 40
        self.pb = ttk.Progressbar(
            master=master,
            orient='vertical',
            length=self.bar_height,
            value=100,
            bootstyle=B_STYLE,

        )
