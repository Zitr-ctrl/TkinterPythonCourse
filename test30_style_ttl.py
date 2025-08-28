import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Python Tkinter Example")
window.geometry("350x150")

# Crear objeto Style
style = ttk.Style()
style.theme_use("xpnative")

# Estilizar todos los widget Button
style.configure("TButton", foreground="red")
style.configure("button1.TButton", foreground="blue")

# Botones
button1 = ttk.Button(window, text="Button 1", style="button1.TButton")
button1.pack(pady=10)

button2 = ttk.Button(window, text="Button 2", style="TButton")
button2.pack(pady=10)

window.mainloop()