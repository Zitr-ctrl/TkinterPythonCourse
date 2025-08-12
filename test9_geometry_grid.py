import tkinter as tk

window = tk.Tk()
window.title("Mi ventana en tkinter")
window.geometry("500x500")

# Etiquetas
element1 = tk.Label(window, text="Etiqueta 1", bg="lightblue", width=10, height=3)
element2 = tk.Label(window, text="Etiqueta 2", bg="lightgreen", width=10, height=3)
element3 = tk.Label(window, text="Etiqueta 3", bg="lightcoral", width=10, height=3)
element4 = tk.Label(window, text="Etiqueta 4", bg="lightyellow", width=10, height=3)
element5 = tk.Label(window, text="Etiqueta 5", bg="lightpink", width=10, height=3)
element6 = tk.Label(window, text="Etiqueta 6", bg="lightgray", width=10, height=3)
element7 = tk.Label(window, text="Etiqueta 7", bg="gold", width=10, height=3)

# Posicionamiento de las etiquetas en grid
element1.grid(row=0, column=0)
element2.grid(row=0, column=1, rowspan=3, sticky="ns")
element3.grid(row=0, column=2)
element4.grid(row=1, column=0)
element5.grid(row=1, column=2)
element6.grid(row=2, column=0)
element7.grid(row=2, column=1)


window.mainloop()