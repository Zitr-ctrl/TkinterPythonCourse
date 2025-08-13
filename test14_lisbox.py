import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("500x200")
# Ventana no minimizable
window.minsize(500, 200)

# Listbox
list = tk.Listbox(window,selectmode=tk.BROWSE ,height=10, width=50)
list.pack()

# lista de elementos
elements = ["Rojo", "Verde", "Azul", "Amarillo", "Rosa", "Gris", "Cian", "Amarillo"]

# insertar opciones
list.insert(0, *elements)

# obtener el valor total de elementos
element = list.size()
print(f"Total de elementos: {element}")

# obtener un elemento de la lista
element = list.get(2)
print(f"Elemento seleccionado: {element}")

# Eliminar un elemento de la lista
#list.delete(2)

# Configuración especifica de un elemento
list.itemconfigure(2, selectbackground="blue", selectforeground="white")

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()