import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Python Tkinter Example")
window.geometry("350x150")

def reaction(event):
    selection = combo.get()
    print("Opcion seleccionada:", selection)

options = ["Rojo", "Verde", "Azul"]

combo = ttk.Combobox(window, values=options, state="normal")
combo.pack(pady=10)

def process():
    text = combo.get()
    if text and text not in combo['values']:
        new_options = list(combo['values']) + [text]
        combo['values'] = new_options
        combo.set(text)
    else:
        print("Seleccionaste:", text)

button = tk.Button(window, text="Agregar", command=process)
button.pack(pady=5)

window.mainloop()