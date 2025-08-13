import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("500x500")
# Ventana no minimizable
window.minsize(500, 500)

# Etiquetas
element1 = tk.Label(window, text="Elemento 1", bg="lightblue")
element2 = tk.Label(window, text="Elemento 2", bg="lightgreen")
element3 = tk.Label(window, text="Elemento 3", bg="lightcoral")
element4 = tk.Label(window, text="Elemento 4", bg="lightyellow")
element5 = tk.Label(window, text="Elemento 5", bg="lightblue")
element6 = tk.Label(window, text="Elemento 6", bg="lightgreen")

# Posicionamiento de las etiquetas en grid
element1.grid(row=0, column=0, sticky="nsew")
element2.grid(row=0, column=1, sticky="nsew")
element3.grid(row=0, column=2, sticky="nsew")
element4.grid(row=1, column=0, sticky="nsew")
element5.grid(row=1, column=1, sticky="nsew")
element6.grid(row=1, column=2, sticky="nsew")

# Configuración responsiva del grid
window.columnconfigure(0, weight=1, minsize=100)
window.columnconfigure(1, weight=1, minsize=100)
window.columnconfigure(2, weight=1, minsize=100)

# Configuración responsiva para las filas
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()