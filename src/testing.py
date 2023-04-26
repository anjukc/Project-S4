import tkinter as tk

# Create a new window
window = tk.Tk()

# Add a label to the window
label = tk.Label(window, text="Hello, GUI World!")
label.pack()

# Add a button to the window
button = tk.Button(window, text="Click Me!")
button.pack()

# Start the GUI event loop
window.mainloop()