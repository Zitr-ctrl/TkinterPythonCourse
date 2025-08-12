# importar tkinter
import tkinter as tk

window = tk.Tk()
window.title("Mi ventaana en tkinter") 
window.geometry("500x300+600+350")

# Widget Text
text = tk.Text(window, width=50, height=15)
text.pack()

# Funcion para obtener la posición del cursor
def cursor_position(event):
    # Obtener la posicion del cursor
    position = text.index(tk.INSERT)
    print("Posicion del cursor:", position)  # Imprimir la posición en la consola

# Asociar las pulsaciones de teclas
text.bind("<KeyRelease>", cursor_position)


# Bucle principal
window.mainloop()