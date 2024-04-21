from random import randint, choice
from ttkbootstrap import ttk
import tkinter as tk


class Bar(tk.Canvas.create_rectangle()):
    def __init__(self, **kwargs: dict) -> None:
        win_height = kwargs['win_height']
        height = randint(1, 100)
        height_pct = height / 100
        self.bar_height = round(height_pct * win_height) - 40
        self.bar_color = "%06x" % randint(0, 0xFFFFFF)

    def create_bar(self, **kwargs):
        return self.create_rectangle((5, self.bar_height, 25, 5), fill=self.bar_color, width=2)
