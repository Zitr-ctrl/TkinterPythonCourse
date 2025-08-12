import tkinter as tk

window = tk.Tk()

# Titulo de la ventana
window.title("Este es mi titutlo de ventana")
# Tamaño de la ventana
window.geometry("500x300+600+350")

# Función para insertar texto en el widget Text

text= tk.Text(window, width=50, height=15)
text.pack()

#Función para eliminar texto
def text_get():
    # Obtener el texto desde el inicio hasta el fin
    content = text.get("1.0", tk.END)
    selection = text.get("1.0", "1.end")
    print("Contenido:\n " + content)  # Imprimir el contenido en la consola
    print("Selección:\n " + selection)  # Imprimir la selección en la consola

# Botón para insertar texto
insert_button = tk.Button(window, text="Obtener texto", command=text_get)
insert_button.pack()

window.mainloop()