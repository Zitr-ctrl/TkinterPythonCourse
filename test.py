import tkinter as tk

# Se crea el objeto de la ventana principal
window = tk.Tk()
# Titulo de la ventana
window.title("Python: Intefaz Gráfica")
# Tamaño de la ventana
window.geometry("500x300+600+350")

# Creamos una fuente personalizada
custom_font = ("Roboto", 36, "bold")

window.config(cursor="hand1")
# Todo lo que hagamos
#label = tk.Label(text="Hola Mundo!", background="lightblue", foreground="black", font=custom_font, cursor="hand2")


# Botón
#boton = tk.Button(window, text="¡haz Click¡", font=custom_font, background="red", foreground="white", cursor="hand2", relief="solid", bd=5)

# Entrada de texto
entrada = tk.Entry(window, font="helvetica", bd=3, relief="groove")

# Muestra la etiqueta en la ventana
#label.pack()
#boton.pack()
entrada.pack()

entrada.config()

# bucle principal de la ventana
window.mainloop()

