from tkinter import *
import random

GAME_WIDTH = 900
GAME_HEIGHT = 500
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title('Sorting Visualizer')
window.resizable(False, True)

BAR_COUNT = tuple(range(50))

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window.mainloop()
