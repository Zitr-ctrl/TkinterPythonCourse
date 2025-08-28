import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("400x100")

def show_value(value):
    print("Valor seleccionado: ", value)

scale = tk.Scale(window, from_=0, to=100, showvalue=True, orient="horizontal", command=show_value)
scale.pack(fill='x', padx=10, pady=10)

window.mainloop()