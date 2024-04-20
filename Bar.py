from random import randint
from tkinter import ttk
import tkinter as tk


class Bar:
    def __init__(self, master: tk.Tk, win_height: int) -> None:
        height = randint(1, 100)
        height_pct = height / 100
        # print(height_pct)
        self.bar_height = round(height_pct * win_height) - 40
        print(self.bar_height)
        self.pb = ttk.Progressbar(
            master=master,
            orient='vertical',
            length=self.bar_height,

        )
