import tkinter as tk

window = tk.Tk()
window.title("My Spinbox Example")
window.geometry("300x200")

var = tk.IntVar(value=10)

spinbox = tk.Spinbox(window, from_=0, to=50, increment=1, textvariable=var)
spinbox.pack(pady=20)

def show_value():
    print("Valor actual:", var.get())

button = tk.Button(window, text="Mostrar valor", command=show_value)
button.pack(pady=10)

window.mainloop()