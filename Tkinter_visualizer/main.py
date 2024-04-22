import time
import tkinter as tk
from random import shuffle
from tkinter import ttk
from Bar import Bar


def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1, len(array))):
        heap_swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)


def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)


def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx].bar_height > heap[childOneIdx].bar_height:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap].bar_height > heap[currentIdx].bar_height:
            heap_swap(currentIdx, idxToSwap, heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return


def heap_swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    updateBarPosition()


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


def quickSort(array: list) -> None:
    quickSortHelper(array, 0, len(array) - 1)


def quickSortHelper(array: list, startIdx: int, endIdx: int) -> None:
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx].bar_height > array[pivotIdx].bar_height > array[rightIdx].bar_height:
            quick_swap(leftIdx, rightIdx, array)
        if array[leftIdx].bar_height <= array[pivotIdx].bar_height:
            leftIdx += 1
        if array[rightIdx].bar_height >= array[pivotIdx].bar_height:
            rightIdx -= 1
    quick_swap(pivotIdx, rightIdx, array)
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def quick_swap(i: int, j: int, array: list) -> None:
    array[i], array[j] = array[j], array[i]
    updateBarPosition()


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
    # bubbleSort(bars)
    # insertionSort(bars)
    # selectionSort(bars)
    # quickSort(bars)
    heapSort(bars)


if __name__ == '__main__':
    # window
    window = tk.Tk()
    window.title('Sorting Algorithms')
    wondow_width = 1602
    window_height = 900
    window.geometry(f'{str(wondow_width)}x{str(window_height)}')
    # window.resizable(False, True)

    # grid layout for bars printing
    a = tuple(range(150))
    window.columnconfigure(a, weight=1, uniform='a')
    window.rowconfigure(0, weight=1)

    # list of bars
    height_mul = ((window.winfo_screenheight() - 150) / len(a))
    bars = [Bar(window, i * height_mul) for i in range(len(a))]
    shuffle(bars)

    updateBarPosition()

    sort_button = ttk.Button(master=window, text='Sort', command=sortBars)
    sort_button.grid(row=1, column=1, columnspan=len(a) * 1)

    # sort_button = ttk.Button(master=window, text='test') # , command=sortBars
    # sort_button.grid(row=1, column=2, columnspan=len(a)*2)
    #
    # sort_button = ttk.Button(master=window, text='test') # , command=sortBars
    # sort_button.grid(row=1, column=3, columnspan=len(a)*3)

    # run
    window.mainloop()
