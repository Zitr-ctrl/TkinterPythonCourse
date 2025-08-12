import tkinter as tk

window = tk.Tk()
window.title("Mi ventana en tkinter")
window.geometry("500x500")

# Etiquetas
element1 = tk.Label(window, text="Etiqueta 1: 42.86px (14.29%)", bg="lightblue", width=28)
element2 = tk.Label(window, text="Etiqueta 2: 85.72px (28.57%)", bg="lightgreen", width=28)
element3 = tk.Label(window, text="Etiqueta 3: 42.86px (14.29%)", bg="lightcoral", width=28)
element4 = tk.Label(window, text="Etiqueta 4: 128.57px (42.86%)", bg="lightyellow", width=28)

# Posicionamiento de las etiquetas en grid
element1.grid(row=0, sticky="ns")
element2.grid(row=1, sticky="ns")
element3.grid(row=2, sticky="ns")
element4.grid(row=3, sticky="ns")

# Especificamos el comportamiento de las filas
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=3)

window.mainloop()