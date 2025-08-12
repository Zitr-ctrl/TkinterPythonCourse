import tkinter as tk

window = tk.Tk()

# Titulo de la ventana
window.title("Este es mi titutlo de ventana")
# Tamaño de la ventana
window.geometry("500x300+600+350")

# Función para insertar texto en el widget Text

text= tk.Text(window, width=50, height=15)
text.pack()

# Insertamos algo de texto
text.insert("1.0", "Primera Línea.\n")
text.insert("2.0", "Segunda Línea.\n")
text.insert("3.0", "Tercera Línea.\n")

#Función para eliminar texto
def text_delete():
    text.delete("2.0","2.8")

# Botón para insertar texto
insert_button = tk.Button(window, text="Eliminar texto", command=text_delete)
insert_button.pack()

window.mainloop()