import tkinter as tk

window = tk.Tk()
window.title("My Tkinter Window")
window.geometry("400x200")
# Ventana no minimizable
window.minsize(400, 200)

# Etiquetas
element1 = tk.Label(window, text="Elemento 1", bg="lightblue")
element2 = tk.Label(window, text="Elemento 2", bg="lightgreen")
element3 = tk.Label(window, text="Elemento 3", bg="lightcoral")
element4 = tk.Label(window, text="Elemento 4", bg="lightyellow")
element5 = tk.Label(window, text="Elemento 5", bg="lightpink")


# Posicionamiento de las etiquetas en flex

# element1.place(x=0, y=0, width=160, height=50)
# element2.place(x=170, y=0, width=160, height=50)
# element3.place(x=0, y=60, width=160, height=50)
# element4.place(x=170, y=60, width=160, height=50)

# element1.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
# element2.place(relx=0.30, rely=0, relwidth=0.25, relheight=0.25)
# element3.place(relx=0, rely=0.30, relwidth=0.25, relheight=0.25)
# element4.place(relx=0.30, rely=0.30, relwidth=0.25, relheight=0.25)

element1.place(relx=0, rely=0, anchor="nw", width=160, height=50)
element2.place(relx=1, rely=0, anchor="ne", width=160, height=50)
element3.place(relx=0, rely=1, anchor="sw", width=160, height=50)
element4.place(relx=1, rely=1, anchor="se", width=160, height=50)
element5.place(relx=0.5, rely=0.5, anchor="center", width=160, height=50)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()