import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

# widgets
w = round(600 / 4)
label1 = ttk.Label(window, background='red', width=w)
label2 = ttk.Label(window, background='blue', width=w)
label3 = ttk.Label(window, background='green', width=w)
label4 = ttk.Label(window, background='yellow', width=w)
button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')
entry = ttk.Entry(window)

# define a grid
numberOfColumns = tuple(range(4))
print(numberOfColumns)
window.columnconfigure(numberOfColumns, weight=1)
window.rowconfigure(0, weight=1)

# place a widget
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=0, column=3)

# run
window.mainloop()
