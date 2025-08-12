import tkinter as tk

window = tk.Tk()
window.title("Mi ventana en tkinter")
window.geometry("500x500")

# Creamos los botones
# button1 = tk.Button(window, text="Noroeste").pack(anchor=tk.NW)
# button2 = tk.Button(window, text="Norte").pack(anchor=tk.N)
# button3 = tk.Button(window, text="Noreste").pack(anchor=tk.NE)
# button4 = tk.Button(window, text="Oeste").pack(anchor=tk.W)
# button5 = tk.Button(window, text="Centro").pack(anchor=tk.CENTER)

# Etiqueta
# label_1 = tk.Label(window, text="Etiqueta Expansible", bg="SpringGreen")
# label_2 = tk.Label(window, text="Etiqueta Fija", bg="deep pink")

# label_1.pack(fill="x")
# label_2.pack(fill="both", expand=True)

label_1 = tk.Label(window, text="arriba", bg="SpringGreen")
label_2 = tk.Label(window, text="abajo", bg="deep pink")
label_3 = tk.Label(window, text="izquierda", bg="LightBlue")
label_4 = tk.Label(window, text="derecha", bg="deep pink")

label_1.pack(side="top")
label_2.pack(side="bottom")
label_3.pack(side="left")
label_4.pack(side="right")

window.mainloop()