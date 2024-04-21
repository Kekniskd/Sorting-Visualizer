import tkinter as tk
from random import randint
from tkinter import ttk


def bubbleSort(array: list) -> None:
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx].bar_height > array[idx + 1].bar_height:
                swap(idx, array)
                is_sorted = False
        counter += 1
        # updateBarPosition()
        # window.update()


def swap(idx: int, array: list) -> None:
    array[idx], array[idx + 1] = array[idx + 1], array[idx]
    updateBarPosition()
    window.update()


def updateBarPosition(elements):
    for idx, element in enumerate(elements):
        element.grid(row=0, column=idx, sticky='ews', padx=1, pady=(0, 35))


def sortBars():
    global bars
    bubbleSort(bars)
    # bars.sort(key=lambda barObj: barObj.bar_height)
    # updateBarPosition()


if __name__ == '__main__':
    # window
    window = tk.Tk()
    window.title('Sorting Algorithms')
    wondow_width = 1200
    window_height = 800
    window.geometry(f'{str(wondow_width)}x{str(window_height)}')
    # window.resizable(False, True)

    # grid layout for bars printing
    a = tuple(range(150))
    # window.columnconfigure(a, weight=1, uniform='a')
    # window.rowconfigure(0, weight=1)

    # list of bars
    canvases = []
    bars = []

    canvas = tk.Canvas(window, bg='white')
    for _ in range(len(a)):
        bar_color = "#%06x" % randint(0, 0xFFFFFF)

        canvas_height = canvas.winfo_height()
        canvas_width = canvas.winfo_width()

        bar_height = randint(1, 100)
        height_pct = bar_height / 100
        bar_height = round(height_pct * canvas_height) - 40
        bar_height = canvas_height - bar_height

        check = 20
        canvas.create_rectangle((20, canvas_height, 100, 50), fill=bar_color, width=2)
        canvases.append(canvas)

    updateBarPosition(canvases)

    sort_button = ttk.Button(master=window, text='Sort', command=sortBars)
    sort_button.place(relx=0.48, rely=0.93)

    # run
    window.mainloop()
