import tkinter as tk

window = tk.Tk()
window.title("Check Button Example")
window.geometry("500x200")

# Creamos los checkbutton

# confirmation_1 = tk.Checkbutton(window, text="Confirmación 1")
# confirmation_1.pack()

# confirmation_2 = tk.Checkbutton(window, text="Confirmación 2")
# confirmation_2.pack()

# confirmation_3 = tk.Checkbutton(window, text="Confirmación 3")
# confirmation_3.pack()


def selection_label():
    tk.Label(window, text=control_variable.get()).pack()

control_variable = tk.StringVar()

# CheckButton
confirmation_1 = tk.Checkbutton(window, text="Confirmación 1", variable=control_variable, onvalue="Opción 1 seleccionada", offvalue="Opción 1 desmarcada")
confirmation_1.pack()
confirmation_1.deselect()

# Boton para mostrar la seleccion
show_selection_button = tk.Button(window, text="Mostrar selección", command=selection_label)
show_selection_button.pack()

window.mainloop()
