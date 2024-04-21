import time
import tkinter as tk
from random import shuffle
from tkinter import ttk
from Bar import Bar


def bubbleSort(array: list) -> None:
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx].bar_height > array[idx + 1].bar_height:
                bubble_swap(idx, array)
                is_sorted = False
            # updateBarPosition()
        counter += 1


def insertionSort(array: list) -> None:
    for idx in range(1, len(array)):
        curr_idx = idx
        while curr_idx > 0 and array[curr_idx].bar_height < array[curr_idx - 1].bar_height:
            insertion_swap(curr_idx, array)
            curr_idx -= 1
        # updateBarPosition()


def selectionSort(array: list) -> list:
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx].bar_height > array[i].bar_height:
                smallestIdx = i
            # updateBarPosition()
        selection_swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def selection_swap(i: int, j: int, array: list) -> None:
    array[i], array[j] = array[j], array[i]
    updateBarPosition()


def insertion_swap(idx: int, array: list) -> None:
    array[idx], array[idx - 1] = array[idx - 1], array[idx]
    updateBarPosition()


def bubble_swap(idx: int, array: list) -> None:
    array[idx], array[idx + 1] = array[idx + 1], array[idx]
    updateBarPosition()


def updateBarPosition():
    global bars
    for _idx, _bar in enumerate(bars):
        _bar.pb.grid(row=0, column=_idx, sticky='ews', padx=1, pady=(0, 35))
    window.update()


def sortBars():
    global bars
    bubbleSort(bars)
    # insertionSort(bars)
    # selectionSort(bars)


if __name__ == '__main__':
    # window
    window = tk.Tk()
    window.title('Sorting Algorithms')
    wondow_width = 900
    window_height = 500
    window.geometry(f'{str(wondow_width)}x{str(window_height)}')
    # window.resizable(False, True)

    # grid layout for bars printing
    a = tuple(range(150))
    window.columnconfigure(a, weight=1, uniform='a')
    window.rowconfigure(0, weight=1)

    # list of bars
    height_mul = window_height / len(a)
    bars = [Bar(window, i * height_mul) for i in range(len(a))]
    shuffle(bars)

    updateBarPosition()

    sort_button = ttk.Button(master=window, text='Sort', command=sortBars)
    sort_button.place(relx=0.48, rely=0.93)

    # run
    window.mainloop()
