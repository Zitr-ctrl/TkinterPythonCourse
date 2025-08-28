import tkinter as tk

window = tk.Tk()
window.title("geometry Event")
window.geometry("400x200")

def size_update(event):
    # Obtener el tamaño de la ventana
    width = event.width
    height = event.height
    label.config(text=f"tamaño: {width}x{height}")


# Etiqueta
label = tk.Label(window, text="Tamaño: 400x200")
label.pack(expand=True, fill=tk.BOTH)

# Asociar ventana
window.bind("<Configure>", size_update)

window.mainloop()