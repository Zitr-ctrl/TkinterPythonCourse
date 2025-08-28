import tkinter as tk

window = tk.Tk()
window.title("Menu Example")
window.geometry("300x200")

menu_bar = tk.Menu(window)

# Menú Archivo
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Abrir")
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)

# Menú Editar
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Deshacer")
edit_menu.add_command(label="Rehacer")


export_menu = tk.Menu(menu_bar, tearoff=0)
export_menu.add_command(label="Exportar como PDF")
export_menu.add_command(label="Exportar como Imagen")

# check buttons
check_menu = tk.Menu(menu_bar, tearoff=0)
check_menu.add_checkbutton(label="Opción 1")
check_menu.add_checkbutton(label="Opción 2")

# Botones de los menús
menu_bar.add_cascade(label="Archivo", menu=file_menu)
menu_bar.add_cascade(label="Editar", menu=edit_menu)
menu_bar.add_cascade(label="Exportar", menu=export_menu)
menu_bar.add_cascade(label="Opciones", menu=check_menu)

window.config(menu=menu_bar)

window.mainloop()