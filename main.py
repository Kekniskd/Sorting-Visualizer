import tkinter as tk

# Create a basic window
window = tk.Tk()
window.title("Tkinter Test")
window.geometry("300x200")

# Add a label to the window
label = tk.Label(window, text="Tkinter is working!")
label.pack(pady=50)

# Start the main event loop
window.mainloop()
