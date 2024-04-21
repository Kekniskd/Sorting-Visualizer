import tkinter as tk

window = tk.Tk()
window.title('Sorting Algorithms')
wondow_width = 900
window_height = 400
window.geometry(f'{str(wondow_width)}x{str(window_height)}')

for _ in range(10):
    canvas = tk.Canvas(window, bg='blue')
    canvas.pack()

window.mainloop()
