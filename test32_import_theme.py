import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk

root = ThemedTk()

# Cargar el tema desde el archivo TCL
root.tk.call("source", "breeze-dark/breeze-dark/breeze-dark.tcl")

root.set_theme("breeze-dark")

root.title("Python Tkinter Example")
root.geometry("350x150")

label = ttk.Label(root, text="Hello, World!")
label.pack(pady=10)

entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

root.mainloop()