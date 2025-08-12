import tkinter as tk

window = tk.Tk()
window.title("Mi ventana en tkinter")
window.geometry("500x500")

# Creamos un marco
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

# Configuramos los marcos
frame1.config(bg="RoyalBlue", width=100, height=100, border=3, cursor="cross")
frame2.config(bg="red", width=100, height=100, border=3, cursor="cross")
frame3.config(bg="green", width=100, height=100, border=3, cursor="cross")
frame4.config(bg="yellow", width=100, height=100, border=3, cursor="cross")

# Empacamos los marcos
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

window.mainloop()