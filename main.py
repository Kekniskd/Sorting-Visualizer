import tkinter as tk
from tkinter import ttk
from Bar import Bar


def updateBarPosition():
    global bars
    for _idx, _bar in enumerate(bars):
        _bar.pb.grid(row=0, column=_idx, sticky='ews', padx=1, pady=(0, 35))


def sortBars():
    global bars
    bars.sort(key=lambda barObj: barObj.bar_height)
    updateBarPosition()


if __name__ == '__main__':
    # window
    window = tk.Tk()
    window.title('Sorting Algorithms')
    wondow_width = 900
    window_height = 400
    window.geometry(f'{str(wondow_width)}x{str(window_height)}')
    # window.resizable(False, True)

    # grid layout for bars printing
    a = tuple(range(10))
    window.columnconfigure(a, weight=1, uniform='a')
    window.rowconfigure(0, weight=1)

    # list of bars
    bars = [Bar(window, window_height) for _ in range(len(a))]

    updateBarPosition()

    sort_button = ttk.Button(master=window, text='Sort', command=sortBars)
    sort_button.place(relx=0.48, rely=0.93)

    # run
    window.mainloop()
