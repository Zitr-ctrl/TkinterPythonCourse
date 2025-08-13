import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("500x200")
# Ventana no minimizable
window.minsize(500, 200)

# crear un widget Scrollbar
scrollbar_y = tk.Scrollbar(window)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

# scrollbar_x = tk.Scrollbar(window, orient=tk.HORIZONTAL)
# scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# text = tk.Text(window, height=10, width=50, yscrollcommand=scrollbar_y.set) #, xscrollcommand=scrollbar_x.set
# text.pack(side="left", fill="both", expand=True)

# # Configurar el scrollbar para que controle el widget de texto
# scrollbar_y.config(command=text.yview)


# Ejemplo de in listbox con scrollbar
list = tk.Listbox(window, yscrollcommand=scrollbar_y.set)
list.pack(side="left", fill="both", expand=True)

# Añadir elementos a la lista
for i in range(50):
    list.insert(tk.END, f"Elemento {i+1}")

# Configurar la barra de desplazamiento para que controle el listbox
scrollbar_y.config(command=list.yview)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()