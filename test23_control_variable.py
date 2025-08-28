import tkinter as tk

window = tk.Tk()
window.title("Control de Variable")
window.geometry("500x200")

name_var = tk.StringVar() # Variable de control de texto

tk.Label(window, text="Ingrese un texto:").pack(pady=10)
entry = tk.Entry(window, textvariable=name_var)
entry.pack()

label = tk.Label(window, textvariable=name_var)
label.pack()


window.mainloop()