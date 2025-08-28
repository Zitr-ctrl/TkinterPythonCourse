import tkinter as tk

window = tk.Tk()
window.title("Eventos Temporales")
window.geometry("500x100")

# Etiqueta para mensajes
label = tk.Label(window, text="", font=("Arial", 24))
label.pack(pady=20)

#Evento

def greet():
    label.config(text="¡Hola, usuario!")

# Con el metodo after se puede programar el tiempo en el que se ejecutara un evento
window.after(5000, greet)

window.mainloop()

