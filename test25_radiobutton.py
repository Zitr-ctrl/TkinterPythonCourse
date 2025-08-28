import tkinter as tk

window = tk.Tk()
window.title("Radio Button Example")
window.geometry("500x200")

# Variable de control
control_variable = tk.IntVar()

def update_radio(value):
    tk.Label(window, text=value).pack()

# Radiobutton
option_1 = tk.Radiobutton(window, text="Opción 1", variable=control_variable, value=1)
option_1.pack()

option_2 = tk.Radiobutton(window, text="Opción 2", variable=control_variable, value=2)
option_2.pack()

option_3 = tk.Radiobutton(window, text="Opción 3", variable=control_variable, value=3)
option_3.pack()

option_4 = tk.Radiobutton(window, text="Opción 4", variable=control_variable, value=4)
option_4.pack()

button_submit = tk.Button(window, text="Enviar", command=lambda: update_radio(control_variable.get()))
button_submit.pack()

window.mainloop()