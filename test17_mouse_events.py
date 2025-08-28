import tkinter as tk

window = tk.Tk()
window.title("Mouse Events")
window.geometry("500x100")

def click(event):
    print("Mouse clicked at")
    label = tk.Label(window, text="Haz dado click")
    label.pack()

def button_left(event):
    print("Mouse left the button")
    label = tk.Label(window, text="botón izquierdo")
    label.pack()

def button_right(event):
    print("Mouse right the button")
    label = tk.Label(window, text="botón derecho")
    label.pack()

def button_center(event):
    print("Mouse centered the button")
    label = tk.Label(window, text="botón central")
    label.pack()

# Botón
button = tk.Button(window, text="Click Me")
button.pack()

button.bind("<Button-1>", button_left)
button.bind("<Button-3>", button_right)
button.bind("<Button-2>", button_center)

window.mainloop()