import tkinter as tk

def foco_activo(evento):
    label.config(text="Foco activo en el botón")

def foco_inactivo(evento):
    label.config(text="Foco inactivo en el botón")

window = tk.Tk()
window.title("Mouse Events Example")
window.geometry("500x200")

# Campo de entrada 
entrada = tk.Entry(window)
entrada.pack(pady=20)

# Botón
button = tk.Button(window, text="Presiona aquí")
button.pack(pady=20)

# Etiqueta
label = tk.Label(window, text="Coloca el foco en el botón para ver el estado.")
label.pack(pady=10)

# Asociación de los eventos de enfoque con el botón
button.bind("<FocusIn>", foco_activo)
button.bind("<FocusOut>", foco_inactivo)

window.mainloop()